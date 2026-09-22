"""
K-pop 월드투어 공연 실적 가상 데이터 생성 (business_data.csv)
- 1행 = 공연 1회
- pandas, numpy만 사용
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 250

# ── 1. 기준 정보 ─────────────────────────────────────────
# 아티스트별 인기도(흥행력 계수)와 공연 비중 (가상의 그룹명)
artists = {
    "NOVA":    {"pop": 1.30, "w": 0.26},
    "LUMINA":  {"pop": 1.10, "w": 0.24},
    "BLAZE":   {"pop": 1.00, "w": 0.20},
    "ECHO9":   {"pop": 0.85, "w": 0.17},
    "STARLIT": {"pop": 0.70, "w": 0.13},   # 신인급
}
# 권역별 기준 티켓가(USD)와 공연 비중
regions = {
    "국내":   {"base": 110, "w": 0.22},
    "일본":   {"base": 130, "w": 0.24},
    "동남아": {"base":  95, "w": 0.18},
    "북미":   {"base": 160, "w": 0.18},
    "유럽":   {"base": 140, "w": 0.11},
    "중남미": {"base": 105, "w": 0.07},
}
# 공연장 규모별 수용인원 범위와 가격 계수
venues = {
    "홀":       {"cap": (2000, 5000),   "pf": 0.90},
    "아레나":   {"cap": (8000, 20000),  "pf": 1.00},
    "스타디움": {"cap": (30000, 60000), "pf": 1.15},
}

# ── 2. 범주형 컬럼 ───────────────────────────────────────
artist_names = list(artists)
artist = rng.choice(artist_names, size=N, p=[artists[a]["w"] for a in artist_names])

region_names = list(regions)
region = rng.choice(region_names, size=N, p=[regions[r]["w"] for r in region_names])

def pick_venue(a):
    pop = artists[a]["pop"]
    if pop >= 1.2:   p = [0.10, 0.55, 0.35]
    elif pop >= 1.0: p = [0.20, 0.65, 0.15]
    else:            p = [0.55, 0.43, 0.02]
    return rng.choice(list(venues), p=p)

venue_type = np.array([pick_venue(a) for a in artist])

# ── 3. 날짜 (2024~2025, 여름·가을 성수기 가중) ───────────
days = pd.date_range("2024-01-01", "2025-12-31", freq="D")
month_w = {1: .5, 2: .6, 3: .8, 4: 1.0, 5: 1.1, 6: 1.2,
           7: 1.4, 8: 1.5, 9: 1.3, 10: 1.2, 11: 1.0, 12: 0.9}
p_day = np.array([month_w[d.month] for d in days], dtype=float)
p_day /= p_day.sum()
show_date = pd.to_datetime(rng.choice(days, size=N, p=p_day))

# ── 4. 수치형 컬럼 ───────────────────────────────────────
pop = np.array([artists[a]["pop"] for a in artist])
base = np.array([regions[r]["base"] for r in region])
pf = np.array([venues[v]["pf"] for v in venue_type])

capacity = np.array([rng.integers(*venues[v]["cap"]) for v in venue_type])
capacity = (capacity // 100) * 100

# 티켓가: 권역 기준가 × 공연장 계수 × 인기도 × 노이즈
price = base * pf * np.sqrt(pop) * rng.lognormal(0, 0.12, N)

# 점유율: 인기도↑ → 점유율↑ / 가격이 권역 기준 대비 비쌀수록 ↓ / 큰 공연장일수록 ↓
size_penalty = np.select([venue_type == "스타디움", venue_type == "아레나"], [0.08, 0.03], 0.0)
occ = (0.78 + 0.25 * (pop - 1) - 0.35 * (price / (base * pf) - 1)
       - size_penalty + rng.normal(0, 0.06, N))
occ = np.clip(occ, 0.40, 1.00)

revenue = capacity * occ * price * rng.uniform(0.97, 1.03, N)

df = pd.DataFrame({
    "show_date": show_date,
    "artist": artist,
    "region": region,
    "venue_type": venue_type,
    "capacity": capacity,
    "avg_ticket_price": price.round(1),
    "occupancy_rate": (occ * 100).round(1),   # 단위: %
    "revenue": revenue.round(0),              # 단위: USD
}).sort_values("show_date").reset_index(drop=True)

# ── 5. 이상치 주입 (현업에서 자주 보이는 입력 오류 패턴) ──
jp_idx = df.index[df["region"] == "일본"][5]
df.loc[jp_idx, "avg_ticket_price"] = 15800.0          # 엔화를 USD로 환산하지 않고 입력
df.loc[40, "occupancy_rate"] = 128.4                   # 점유율 100% 초과
df.loc[150, "revenue"] = df.loc[150, "revenue"] * 10   # 매출 단위/자릿수 오입력
outlier_idx = {jp_idx, 40, 150}

# ── 6. 결측치 주입 (이상치 행은 제외) ────────────────────
candidates = np.array([i for i in df.index if i not in outlier_idx])
for col, ratio in [("occupancy_rate", 0.05), ("avg_ticket_price", 0.04), ("venue_type", 0.03)]:
    k = int(round(N * ratio))
    df.loc[rng.choice(candidates, size=k, replace=False), col] = np.nan

df.to_csv("business_data.csv", index=False, encoding="utf-8-sig")
print(f"저장 완료: business_data.csv ({df.shape[0]}행 × {df.shape[1]}열)")

# 이후 분석은 아래처럼 불러와서 시작
df = pd.read_csv("business_data.csv", parse_dates=["show_date"])
print(df.head())