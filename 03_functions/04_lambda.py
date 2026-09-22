from functools import reduce
def double1(x):
    return x*2

print(f"일반 함수:{double1(77)}")

double2=lambda x: x*2
print(f"람다 함수:{double2(77)}")


print("고차함수")
#map() : 전달한 함수를 적용하여 새로운 이터레이터 반환
numbers=[n for n in range(1,7)]
print(f"numbers:{numbers}")
result=list(map(lambda x:x*2,numbers))
print(f"map 활용 : {result}")

# filter() : 조건을 만족하는 요소만 가지고 새로운 이터레이터를 반환
result=list(filter(lambda x:x % 2==0,numbers))
print(f"filter적용 : {result}")

#sorted() : 데이터를 정렬
numbers=[15,26,7,3,41,17]
print(f"numbers:{numbers}")
print(f"오름차순 정렬: numbers:{sorted(numbers)}")
print(f"내림차순 정렬: numbers:{sorted(numbers,reverse=True)}")

products=[
    {"name":"로지텍 키보드","price":20000 },
    {"name":"손목 쿠션","price":1000 },
    {"name":"레이저 마우스","price":150000 },
]
print(f"products:{products}")

#가격(price) 기준으로 내림차순 정렬
by_price = sorted(products,reverse=True,key=lambda x:x['price'])
for p in by_price:
    print(f"{p['name']}:{p['price']}")
print()
#이름(name) 기준으오 오름차순 정렬
by_name=sorted(products,key=lambda x:x['name'])
for p in by_name:
    print(f"{p['name']}:{p['price']}")

print()

#reduce : 순회하면서 누적 계산을 수행하는 함수
numbers=[10,20,30]
print(reduce(lambda total,curr:total+curr,numbers,0))
datas =["apple","cat","strawberry","moon"]
#가장긴 문자열 찾기
print(reduce(lambda result,curr:result if len(result)>=len(curr) else curr,datas))

numbers=[4,6,7,3,9,8]
print(f"numbers:{numbers}")
print(f"길이: {len(numbers)}")
print(f"총합: {sum(numbers)}")
print(f"최댓값: {max(numbers)}")
print(f"최솟값: {min(numbers)}")

print(f"any:{any(n>5 for n in numbers)}")
print(f"all:{all(n>5 for n in numbers)}")
