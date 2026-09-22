"""
튜플(tuple)
"""

point=(10,20)
point2=50,60

single=(10,) #데이터가 1개일때 콤마 필수
single2=(10)
print(f"point : {point} {type(point)}")
print(f"point : {point2} {type(point2)}")
print(f"single : {single} {type(single)}")
print(f"single2 : {single2} {type(single2)}")
print()

print(f"point[0] : {point[0]}")
#point[0]=99
print(f"point[0] : {point[0]}")

point=(99,20)
print(f"point 자체를 변경 : {point}")

x,y=(2,6)
print(f"x,y:{x},{y}")

def get_numbers():
    return 77,44

x,y=get_numbers()
print(f"x,y:{x},{y}")
x, _, z=(10,20,30)
print(f"x,z:{x},{z}")
x, *rest=(1,2,3,4,5)
print(f"x:{x},rest:{rest}")          

locations={
    (35.5451, 126.9750): "서울역",
    (30.5401, 124.9050): "부산역"
}

