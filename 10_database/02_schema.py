"""
    수집 데이터를 위한 스키마설계
"""

from _db import connect

conn=connect()

def drop_table(cur,name):
    """전달된 테이블을 삭제하는 함수"""
    try:
        cur.execute(f"DROP TABLE {name}")
    except Exception as e:
        if "ORA-00942" not in str(e):
            pass

