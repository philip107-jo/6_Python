"""
    집합 set
"""

nums={1,2,3,3,3,4,2}
print(nums)

empty1={}
empty2=set()
print(f"empty1: {type(empty1)}")
print(f"empty2: {type(empty2)}")

nums=[1,2,3,3,3,4,2]
print(f"원본 데이터: {nums}")
print(f"중복제거: {set(nums)}")
print(f"중복제거: {list(set(nums))}")
print()

a={1,2,3,4}
b={3,4,5,6}

print(f"합집합 | : {a | b}")
print(f"교집합 & : {a & b}")
print(f"차집합 - : {a - b}")
print(f"대칭차집합 ^: {a ^ b}")

data={1,2}
print(f"data: {data}")
data.add(3)
print(f"data: {data}")

data.update([4,5])
print(f"data: {data}")
data.update([4,5,6,7])
print(f"data: {data}")

data.discard(1)
print(f"data: {data}")

