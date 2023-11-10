# DAO : Database Access Object
#     - 데이터 작업(CRUD)을 하는 객체

# 예시)
# 회원 -> member_dao
#         ㄴ 회원가입, 회원수정, 회원조회, 회원검색, 회원삭제

# 로그인 -> login_dao
#         ㄴ 로그인, 로그아웃, ID찾기, PW찾기

from pymongo import MongoClient
def conn_mongodb():
    # IP, PORT, ID, PW
    # URL, ID, PW
    DB_ID = "root"  # 상수(전체 대문자로 변수명을 사용)
    DB_PW = "1234"      # 예시) 은행에서 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.wsjhzgh.mongodb.net/")
    db = client["daum"]
    collection = db.get_collection("news")
    return collection

# 뉴스(제목, 본문, 날짜) 저장

def add_news(data):
    conn = conn_mongodb()   # 1. Connection
    conn.insert_one(data)   # 2. DB에 저장