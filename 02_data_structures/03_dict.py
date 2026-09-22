"""
딕셔너리(dict)
"""

#JSON 형식과 유사한 구조
# key-value 형태로 데이터를 관리

user = {
    "name":"조빌립",
    "age":20,
    "skills":["java","sql","html/css","js","python"]

}
print(f"user:{user}")

print(f"이름: {user['name']}")
print(f"스킬: {user['skills']}")

#print(f"연락처: {user['phone']}")

print()

print(f"이름:{user.get('name')}")
print(f"스킬:{user.get('skills')}")
print(f"연락처:{user.get('phone')}")
print(f"연락처:{user.get('phone','없음')}")
print()

user['email']='sdsa@sd.com'
print(f"{user}")

user['age']=40
print(f"{user}")

del user['age']
print(f"{user}")

#del user['phone']
print(f"{user}")
print()

for key in user:
    print(f"key:{key} / value: {user[key]}")

for k,v in user.items():
    print(f"key: {k} / value: {v}")
print()

print(f"키 목록: {list(user.keys())}")
print(f"밸류 목록: {list(user.values())}")
print(f"items(): {list(user.items())}")