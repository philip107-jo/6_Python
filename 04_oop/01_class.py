"""
    클래스와 객체

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
"""

# 기본형태
class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        return self.balance

acc=Account("조빌립",10000)

print(f"owner: {acc.owner}")
print(f"balance : {acc.balance}")

print(f"deposit : {acc.deposit(7000)}")

#인스턴스 변수 vs 클래스 변수
class Member:
    #클래스 변수 : 모든 인스턴스 공유
    team_name = "리센느"
    count=0

    #생성자
    def __init__(self,name):
        self.name=name   #인스턴스 변수
        Member.count+=1 #클래스 변수는 클래스 명으로 접근

m1=Member("원이")
m2=Member("미나미")

print(f"m1.name:{m1.name}")
print(f"m2.name:{m2.name}")
print(f"m1.team_name:{m1.team_name}")
print(f"m2.team_name:{m2.team_name}")

print(f"Member.count:{Member.count}")

m1.team_name="RESCENE"    #인스턴스에 클래스변수명으로 값을 대입하는경우, 새로운 인스턴스 변수생성
print(m1.team_name)
print(Member.team_name)
