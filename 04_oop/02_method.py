"""
    메소드: 클래스 내의 함수

    -종류-
    * 인스턴스 메소드
    * 클래스 메소드
    * 정적 메소드
"""

class Account:
    bank_name = "KH 은행"
    MIN_DEPOSIT =1000

    def __init__(self, owner,balance=0):
        self.owner=owner
        self.balance=balance
    #인스턴스 메소드 : 객체의 데이터를 다룸.첫번째 매개변수 self
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    # 클래스 메소드: 클래스 자체를 다룸. 첫번째 매개변수 cls
    @classmethod
    def from_dict(cls,data):
        """
            딕셔너리로부터 객체를 생성하는 메소드
        """
        return cls(data["owner"],data.get("balance",0))
    #정적 메소드 : 객체,클래스와 무관한 기능을 담당하는 메소드(유틸리티). @staticmethod
    @staticmethod
    def is_valid_amount(amount):
        return amount >= Account.MIN_DEPOSIT
acc=Account("조빌립",10000)
print(f"deposit --> {acc.deposit(3000)}")

#클래스메소드 호출
acc2=Account.from_dict({"owner":"홍길동","balance":10000})
print(acc2.owner,acc2.balance)

#정적 메소드 호출
print(Account.is_valid_amount(6000))

amount=1500
if Account.is_valid_amount(amount):
    print(acc2.deposit(amount))
else:
    print(f"최소금액을 만족하지 않습니다.")


response=[
    {"owner":"조빌립","balance": "20000"},
    {"owner":"김철수"},
    {"owner":"김빌립","balance": "55000"},
]
accounts=[Account.from_dict(item) for item in response]

for a in accounts:
    print(f"{a.owner} {a.balance}원")

#from_dict활용하면 딕셔너리 구조를 자연스럽게 클래스에 넘겨서 객체를 생성할 수 있음
# 데이터 구조가 변경되거나 메소드를 수정하는 경우 새로 정의해서 대응가능함
