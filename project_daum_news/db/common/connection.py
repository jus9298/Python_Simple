# 파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
# 데이터베이스: 데이터를 효율적으로 저장하고 관리해주는 시스템(이론)

# 데이터베이스 관리 시스템: DBMS. DB제품

# ** DBMS 종류
# 1. 관계형 데이터베이스(RDB) : 전통적인(스키마:명세서)
#     - ORACLE ..유료
#     - MySQL ..무료
#     - MariaDB
#
# 2. NoSQL : New(빅데이터)
#     - MongoDB
#     - Redis

# ** DBMS 프로세스
#     - DB에 ID, PW 저장
# Pycharm(Python) ----------------DB(MongoDB)
#     1. Pycharm과 DB Connection 맺기
#     - IP : 컴퓨터를 접속 할 수 있는 주소
#     - PORT : 컴퓨터 내에 프로그램의 위치
#     - ID and PW

# 2. SQL을 사용해서 작업(CRUD) 진행
#     - SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용!
#     - RDB(SQL) , NoSQL(SQL 사용안함)
#     CREATE -> INSERT
#     READ -> SELECT
#     UPDATE -> UPDATE
#     DELETE -> DELETE

# ** MongoDB 사용방법 2가지
#     1.직접 설치(Local)
#         -장점 : 사용/관리 편함, 커스터마이징 가능
#         -단점 : 설치과정 복잡, 설정 직접, 컴퓨터 자원 부족
#     2.MongoDB에서 제공하는 Web Cloud 사용
#         - url
#         -장점 : 사용편함, 설치x, 설정x, 컴퓨터 자원x
#         -단점 : 관리x, 커스터마이징x

# ** MongoDB 구조
# 설치 : MongoDB(DBMS) : 시스템
#         ㄴDB(카카오톡) : 폴더
#           ㄴCollection(회원) : 표
#           ㄴCollection(톡)
#           ㄴCollection(친구)
#           ㄴ ...
#         ㄴDB(카카오뱅크): 폴더
#           ㄴCollection(회원)
#           ㄴCollection(계좌)
#           ㄴCollection(대출)
#           ㄴ ...
#         ㄴDB(카카오페이) : 폴더



# > conda activate simple
# > pip install pymongo

def conn_mongodb():
    # IP, PORT, ID, PW
    # URL, ID, PW
    DB_ID = "root"  # 상수(전체 대문자로 변수명을 사용)
    DB_PW = "1234"      # 예시) 은행에서 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.wsjhzgh.mongodb.net/")
    db = client["daum"]
    collection = db.get_collection("news")
    return collection
