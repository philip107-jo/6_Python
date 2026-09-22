import random
#1
"""
def bmi(kg,cm):
    m=float(cm/100)
    return kg/(m*m)
kilogram=int(input("몸무게를 입력하세요(kg):"))
centemeter=int(input("키를 입력하세요(cm)"))
print(f"BMI:{bmi(kilogram,centemeter):.2f}")
"""

#2
"""
sum=0
count=0
while(True):
    num=input("숫자입력(q 입력시 종료):")
    if num=="q":
        break
    num=float(num)
    sum+=num
    count+=1

if count >0:
    avg=sum/count
    print(f"-->평균{avg:.2f}")
else:
    print("-->값이없습니다.")
"""
"""
def count_sentence(sentence):
    lower_words=sentence.lower()
    words=lower_words.split()
    frequency={}
    for f in words:
        frequency[f]=frequency.get(f,0)+1
    return frequency

name=str(input("문장을 입력하세요: "))
result=count_sentence(name)

print()
print("\n[단어 빈도수결과]")
for word,count in result.items():
    print(f"-{word}: {count}회")
"""

#4
"""
def lotto(num):
    print("\n[로또번호 발급결과]")
    for i in range(1,num+1):
        numbers=[]
        while len(numbers)<6:
            n=random.randint(1,45)
            if n not in numbers:
                numbers.append(n)
        print(f"{i}게임:{sorted(numbers)}")

n=int(input("구매할 로또 게임 수를 입력하세요: "))
lotto(n)
"""
#5

def analyze(scores):
    top_name = max(scores, key=scores.get)      # 점수가 가장 높은 '이름'
    low_name = min(scores, key=scores.get)      # 점수가 가장 낮은 '이름'
    average = sum(scores.values()) / len(scores)

    return (top_name, scores[top_name]), (low_name, scores[low_name]), average


data = {
    "홍길동": 85,
    "이순신": 96,
    "강감찬": 72,
    "유관순": 91
}

top, low, avg = analyze(data)        # 튜플 언패킹

print("========== 학생 성적 분석 결과 ==========")
print(f"- 최고 득점자: {top[0]} ({top[1]}점)")
print(f"- 최저 득점자: {low[0]} ({low[1]}점)")
print(f"- 전체 평균: {avg}점")
