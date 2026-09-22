import os 
import json
print(__file__)
print("="*60)
BASE_DIR=  os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

TXT_PATH=os.path.join(BASE_DIR,"_sample.txt")
JSON_PATH=os.path.join(BASE_DIR,"_sample.json")

print(f"TXT_PATH: {TXT_PATH}")
print(f"JSON_PATH : {JSON_PATH}")
print("="*50)
#직접 파일을 처리( with x)
f = open(TXT_PATH,"w",encoding="utf-8")
f.write("금요일,20260911,졸림\n")
f.close()

with open(TXT_PATH,"w",encoding="utf-8") as f:
    f.write("금요일,20260911,슬픔\n")
    f.write("토요일,20260911,한계\n")

print(f"저장완료{os.path.basename(TXT_PATH)}")

with open(TXT_PATH,"r",encoding="utf-8") as f:
    contents=f.read()
print(f"파일 내용----------")
print(contents) 

for line in contents.strip().split("\n"):
    print("****")
    print(line)
print("="*60)

products=[
    {"code":"001123","name": "iPhone Duo","price":3300000},
    {"code":"004123","name": "Galaxy Z Flip8","price":1600000}

]
#JSON으로 저장(쓰기)
with open(JSON_PATH,"w",encoding="utf-8")as f:
    json.dump(products,f,ensure_ascii=False,indent=2)

print(f"저장완료{os.path.basename(JSON_PATH)}")
#print(json.dump(products,f,ensure_ascii=True))

with open(JSON_PATH,"r",encoding="utf-8") as f:
    json_contents = json.load(f)

print(f"type -> {type(json_contents)}")
for c in json_contents:
   # print(f"data type -> {type(c)}")
    print(f"{c['name']}: {c['price']}")