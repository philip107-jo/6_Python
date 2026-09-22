"""
    목록 파싱
"""
from parsers import get_text,get_attr,get_number,parse_rate,parse_stocks
import requests
from bs4 import BeautifulSoup
from config import BASE,TIMEOUT,HEADERS
import requests,json,csv
resp=requests.get(f"{BASE}/stocks?sector=S08",headers=HEADERS,timeout=TIMEOUT)
resp.raise_for_status()  #응답코드가 200이아니면 예외발생

html=resp.text
soup=BeautifulSoup(html,'lxml')

row=soup.select_one("tr.stock-row")
try:
    row.select_one("td.test").text  #해당하는 클래스가없을때
except Exception as e:
    print(f"오류{e}")

print(f"td.test->{get_text(row,'td.test')}")

stocks=parse_stocks(html)
print(f"{'코드':<8}{'종목명':<14}{'섹터':<10}{'현재가':>12}{'등락률':>9}")

for s in stocks:
    print(f"{s['code']:<8}{s['name']:<14}{s['sector']:<10}{s['price']:>12}{s['rate']:>9}")
