"""
    함수
"""
def hello(name):
    return f"{name}님 안녕하세요."

print(hello("조빌립"))

def hello_print(name):
    print(f"{name}님 반갑습니다")

print(hello_print("조빌립"))

def calc(a,b):
    return a+b,a-b,a*b

print(calc(1,2))
add,sub,mul=calc(5,6)
print(f"결과: {add},{sub},{mul}")

def calc_tax(price,rate=0.1):
    """
    부가세를 포함한 최종 금액을 반환하는 함수
    """
    return int(price * (1+rate))

print(f"10000원 ---> {calc_tax(10000):,}")
help(calc_tax)

print(test())
def test():
    return "테스트 함수입니다"