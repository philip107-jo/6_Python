"""
변수와 자료형
"""
name="조빌립"
age=20
height=190
is_tired=True 
temp = None                      

print(f"{name},{age},{height},{is_tired},{temp}")
print(f"{name} : {type(name)}")
print(f"{age} : {type(age)}")
print(f"{height} : {type(height)}")
print(f"{is_tired} : {type(is_tired)}")
print(f"{temp} : {type(temp)}")

value=27
print(f"{value}:{type(value)}")
value="스물"
print(f"{value}:{type(value)}")

x,y,z=10,20,30
print(f"x,y,z-> {x},{y},{z}")