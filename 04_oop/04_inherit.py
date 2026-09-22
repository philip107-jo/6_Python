class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def withdraw(self,amount):
        if amount > self.balance:
            print("잔액이 부족합니다")
            return
        self.balance-=amount
        return amount
    def info(self):
        return f"[{self.owner}] 잔액 : {self.balance:,}원"
class SavingsAccount(Account):
    def __init__(self,owner,balance=0,rate=0.03):
        super().__init__(owner,balance)
        self.rate=rate
    def add_intrest(self):
        interest=int(self.balance * self.rate)
        self.balance+=interest
        return interest
    def info(self):
        return f"{super().info()} / 이율 {self.rate}"
sa=SavingsAccount("짱구",10000)
print(sa.info())
print(f"이자지급{sa.add_intrest()}원")
print(sa.info())

class CheckingAccount(Account):
    FEE = 500

    def withdraw(self,amount):
        total=amount + self.FEE

        if total > self.balance:
            print("잔액이 부족합니다.")
            return
        self.balance -= total
        return amount
    def info(self):
        return f"{super().info()} / 수수료 : {self.FEE} 원"
acc_list=[
    Account("하리보",2000),
    SavingsAccount("마이구미",15000),
    CheckingAccount("박카스",8000)
]

for acc in acc_list:
    print(f"{acc.info()}")

#덕 타이핑
#상속관계가 없어도 같은 메소드를 가지면 동일하게 취급

class CsvExporter:
    def export(self,data):
        return f"csv로 {len(data)}건 저장"

class JsonExporter:
    def export(self,data):
        return f"json으로 {len(data)}건 저장"

exp_list=[
    CsvExporter(),
    JsonExporter()
] 

data=[1,2,3]
for exporter in exp_list:
    print(f"{exporter.export(data)}")

#다중상속 : 여러 부모클래스를 상속할 수 있음

class Loggable:
    def log(self,message):
        return f"[LOG] {message}"

class Serializable:
    def to_dict(self):
        return self.__dict__ #모든필드를 딕셔너리로변환

class Product(Loggable,Serializable):
    def __init__(self,name,price):
        self.name=name
        self.price=price

p=Product("핸드크림",5000)
print(f"{p.log('상품을 생성했습니다.')}")
print(f"dict --> {p.to_dict()}")