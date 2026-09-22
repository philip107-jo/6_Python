print(f"7 + 3 = {7 + 3}")
print(f"7 - 3 = {7 - 3}")
print(f"7 x 3 = {7 * 3}")
print(f"7 / 3 = {7 / 3}")
print(f"7 // 3 = {7 // 3}")
print(f"7 % 3 = {7 % 3}")


members= ["조빌립","홍길동","김철수"]
print(f"{members}")
print(f"'조빌립' 포함여부 -> {'조빌립' in members}")
print(f"'조빌립' 포함여부 -> {'조빌립' not in members}")

x=[1,2,3]
y=[1,2,3]
z=x
print(f"x: {x} / y : {y} / z : {z}")

print(f"배열값 비교 : {x==y}")
print(f"객체 주소 비교:{x is y}")
print(f"x is z : {x is z}")

data=None
print(f"data is none? {data is None}")
print(f"data is not none?{data is not None}")

x=10 
print(f"x: {x}")
x+=5
print(f"x+=5:{x}")