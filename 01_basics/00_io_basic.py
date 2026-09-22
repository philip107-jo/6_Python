print("="*60)
print('기본출력확인')
print("="*60)
print("hello, Python!")
print('반가워, 파이썬!')
print(100)
print(3.14)
print(10+20)
print("2026","09","07",sep="-")

print("첫번째 줄",end=" ")
print("두번째 줄")
print("")

print("="*60)
print("이스케이프 문자")
print("="*60)
name="조빌립"
age=25
height=180.5
print("이번 줄 다음에 출력. \n 한줄 개행")

print("이름: {}, 나이:{},키:{}".format(name,age,height))
print(f"이름:{name}, 나이:{age}, 키:{height}")
print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")

age_str=input("나이입력:")
print(f"입력값:{age_str},타입:{type(age_str)}")

age=int(age_str)
print(f"입력값:{age},타입:{type(age)}")
