# python - pymysql ---------------------- Database
# mariadb = pymysql
# DB: MariaDB
#     - type: 관계형 데이터베이스(RDB)

# **root 계정
#     - 신급 권한을 가지는 계정
#     - RDB는 반드시 root 계정 생성
#     - "DB 관리자" -> root 사용 x, new 계정(권한 많이 부여)
# 예) 문서확인 불가
# 신입사원 -> 회원가입 개발 -> DB계정 생성(권한: 회원테이블 읽기, 쓰기)


import pymysql

def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            db="simple",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursoors.DictCursor
        )
        return conn
    except pymysql.Error as e:
        print(f"MARIADB 연결 실패 {e}")

# we're on our way now
# the truth can be so hard to swallow
# hey now
# cause you got the love, you got the love, lady
# I'm worn out
# cause with every little trick, they try to drag you down
# you don't know why

# port 확인
# 서비스
# MariaDB 동작중인지