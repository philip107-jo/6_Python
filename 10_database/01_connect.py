"""
    DB 연동
"""
import oracledb
import pandas as pd
from _db import connect,get_engine,USER,HOST,PORT,NAME,PWD

conn=connect()
#cursor() => Cursor 객체반환
#   excute(sql) 함수를 통해 쿼리문을 실행한 결과를 반환받을 수 있음
with conn.cursor() as cur:
    cur.execute("SELECT (SELECT banner FROM v$version WHERE ROWNUM <=1) AS v,"
                "sys_context('USERENV','DB_NAME') AS db FROM dual")

#한행짜리 결과:fetchone
    row=cur.fetchone()
print(f"접속 :{USER}@{HOST}:{PORT}/{NAME} ")
print(f"조회결과: v:{row[0]} / db:{row[1]}")

with conn.cursor() as cur:
    cur.execute("BEGIN EXECUTE IMMEDIATE 'DROP TABLE demo_commit';"
                "EXCEPTION WHEN OTHERS THEN IF SQLCODE !=-942 THEN RAISE; "
                "END IF; END;")
    cur.execute("CREATE TABLE demo_commit (id NUMBER,memo VARCHAR2(50))")

c1=connect()
with c1.cursor() as cur:
    cur.execute("INSERT INTO demo_commit VALUES(1,'테스트 1')")
    cur.execute("SELECT COUNT(*) FROM demo_commit")
    print(f"데이터 추가 후 바로확인:{cur.fetchone()[0]}")
c1.close()
c2=connect()
with c2.cursor() as cur:
    cur.execute("SELECT COUNT(*) FROM demo_commit")
    print(f"새로운 커넥션에서 조회:{cur.fetchone()[0]}")
"""
    커믹하지않고,커넥션을 반납했을떄(close) 오류가 발생되지 않았음
    DML 실행한 후에는 트랜잭션 관리를 잘해줘야함
"""
c3=connect()

with c3.cursor() as cur:
    cur.execute("INSERT INTO demo_commit VALUES(2,'테스트 2')")
c3.commit()  #명시적 커밋
c3.close()
c4=connect()
with c4.cursor() as cur:
    cur.execute("SELECT COUNT(*) FROM demo_commit")
    print(f"커밋 후 결과조회: {cur.fetchone()[0]}")
c4.close()

print("=" *50)

#파라미터 바인딩
#executemany(sql,[,,,]):동일한 sql을 사용하는데, 값만 바꿔서 여러번 전달

with conn.cursor() as cur:
    cur.execute("BEGIN EXECUTE IMMEDIATE 'DROP TABLE demo_param';"
                    "EXCEPTION WHEN OTHERS THEN IF SQLCODE !=-942 THEN RAISE; "
                    "END IF; END;")
    cur.execute("CREATE TABLE demo_param (code VARCHAR2(10),price NUMBER)")

    cur.executemany(
        "INSERT INTO demo_param VALUES (:1,:2)",
        [("G0001",24000),("G0002",55000),("G0003",10000)]
    )
conn.commit()
with conn.cursor() as cur:
    cur.execute("SELECT * FROM demo_param WHERE price > :1",(2000,))
    print(f"결과 : {len(cur.fetchall())}행")

"""
    파라미터를 한개만 남기더라도 튜플로 전달하는것을 권장
    변수가 여러개인 경우,문자열을 하나만 전달하게 되면 자동으로 쪼개서 사용함
"""

plain=oracledb.connect(user=USER,password=PWD,dsn=f"{HOST}:{PORT}/{NAME}")

with plain.cursor() as cur:
    cur.execute("SELECT * FROM demo_param WHERE ROWNUM <= 1")
    print(f"기본커서 :{cur.fetchone()}")
plain.close()

#rowfactory : 컬럼 이름으로 데이터 접근
with conn.cursor() as cur:
    cur.execute("SELECT * FROM demo_param WHERE ROWNUM <=1")
    columns=[col[0].lower() for col in cur.description]
    cur.rowfactory= lambda * args:dict(zip(columns,args))

    print(f"rowfactory 설정 후 : {cur.fetchone()}")

print("=" *60)
engine=get_engine()

df=pd.read_sql("SELECT * FROM demo_param ORDER BY price DESC",engine)
print(df)
print(df.info())

with conn.cursor() as cur:
    for t in ["demo_commit", "demo_param"]:
        cur.execute(f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {t}';"
                    "EXCEPTION WHEN OTHERS THEN IF SQLCODE !=-942 THEN RAISE; "
                    "END IF; END;")
conn.close()

print("테이블정리오ㅓㄴ")