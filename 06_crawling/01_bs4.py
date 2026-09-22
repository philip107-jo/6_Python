"""
    BeautifulSoup
    : HTML 및 XML 문서에서 데이터를 쉽게 추출할 수 있도록 해주는 스크래핑 라이브러리

    1.request 로 요청 후 문자열(html,xml)을 응답ㅂ다음
    2.bs4의 find,select 를 활용해서 특정 텍스트를 추출 
"""
import requests
from bs4 import BeautifulSoup
from config import BASE,TIMEOUT,HEADERS

resp=requests.get(f"{BASE}/stocks",headers=HEADERS,timeout=TIMEOUT)
resp.raise_for_status()     #200이 아니면 예외발생
html=resp.text
print(f"{BASE}/stocks       [{resp.status_code}] {len(html):,}자")


soup=BeautifulSoup(html,'lxml')
print(f"title --> {soup.title.text if soup.title else '없음'}")

# 기존에 자바스크립트를 통해 DOM조작한 것처럼 bs 이 같은 역할을함
# select : CSS 선택자를 사용하여 해당 요소들을 반환. 없는경우 []
# select_one : CSS 선택자를 사용하여 해당 요소 1개 반환 없는경우 None

rows_select=soup.select("tr.stock-row")
print(f"tr.stock-row 개수 : {len(rows_select)}")

first=soup.select_one("tr.stock-row")
price_tag=first.select_one("td.col-price")
print(f"td.col-price text : {price_tag.text}")
print(f"td.col-price text : {price_tag.text!r}")
print(f"td.col-price text : {price_tag.get_text(strip=True)!r}")

name_link=first.select_one("td.col-name a")
print(f"name_link['href']: ,{name_link['href']}")
print(f"name_link.get('href'): ,{name_link.get('href')}")

#첫번째 행의 전체 데이터를 추출
for sel in["td.col-code","td.col-name a","td.col-sector",
"td.col-price", "td.col-change","td.col-volume","td.col-market span" 
 ]:
    tag=first.select_one(sel)
    value=tag.get_text(strip=True) if tag else "없음"
    print(f"{sel:<20} {value}")

