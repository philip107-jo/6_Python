"""
스코프

-전역변수: 함수외부에 선언된 변수
-지역변수: 함수 내부에 선언된 변수. 해당
"""

print("=" * 60)


count=0

def increase1():
    count=10
    print(f"count:{count}")

increase1()
print(count)

def increase2():
    global count
    count +=1

increase2()
print(f"count:{count}")

data="-- 전역 --"

def outer():
    data = '-- 바깥 함수(outer) --'

    def inner():
        data='--안쪽 함수(inner) --'

        print(f"**inner :: data - {data}")
    inner()
    print(f" **outer ::data - {data}")
outer()
print(f"**전역에서 확인::data - {data}")