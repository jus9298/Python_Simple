
# 문자열의 이해(String)
# 활용 예: 데이터 분석, 자연어 처리 응용, 사용자로부터 값 입력받을 때 처리용도
#
# 1. 문자열 인덱스(Index)
# - 문자열은 각 문자마다 순서(인덱스) 가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# - 인덱스 시작은 0
# - 인덱스는 공백포함
print("="*200)
print("Python")

# 2. 문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류
#   (Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9]) # Error

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1

# 3. 문자열 슬라이싱
# - lang[3]: 문자 1개만 추출
# - 부분 문자열 추출하고 싶은 경우
# - 시작 인덱스, 끝 인덱스 필요
msg = "Python is all you need"
print(msg[0:6]) #끝인덱스 +1
print(msg[:6]) #시작 인덱스 생략 -> 자동 0입력
print(msg[3:]) #끝 인덱스 생략 -> 자동 -1입력
print(msg[:]) #처음부터 끝까지


# Quiz
# msg에서 "need"만 추출
# 정방향
# 역방향

print(msg[18:22])
print(msg[-4:])



# 프로그래밍 언어!
# 컴퓨터계열 학과 -> 프로그래밍 언어 1개는 마스터
# - 여러분들이 아이디어가 떠올랐을 때
#   바로 구현은 못하지만 구글링해서 어떻게
#   어떻게하면 만들 수 있겠네라는 생각이 들 정도

# 개발자: 웹 개발자 (프론트엔드, 백엔드)
# 앱 개발자 (Android, ios)
# 웹 퍼블리셔
# 웹 디자이너
# 인공지능 개발자
# ERP 엔지니어
# 로봇...?
# 서버 엔지니어 (Linux)
# 데이터베이스 엔지니어
# 데이터베이스 관리자
# SQL 튜너
# 데이터 모델러
# 네트워크 엔지니어
# 데이터 엔지니어
# 보안 개발자
# 데이터 분석가, 데이터 사이언티스트
# 빅데이터 서버 엔지니어

# 다해봐 개발환경구축, 개발도 해보고 1년도안걸려
# 적성에 안맞는거 지워


# 4. 문자열 함수
str = "Hello World"

# 4-1.len() : 문자열 길이 계산
print(len(str))

# 4-2. upper() and lower() : 대소문자 변경
# - ID = "ChoLong02" -> "ChoLong02".lower()
# - 데이터 전처리 -> 1A, 1a -> upper() 1A 통일
print(str.upper())
print(str.lower())

# 4-3. replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4. split() : 구분자를 기준으로 문자열 분할(Default: 공백)
b = "hello world what a nice weather"
print(b.split())
print(b.split("w"))

# 4-5. strip() : 문자열의 좌우 공백 제거
id = "                  python1004        "
print(id)
print(id.strip())

#id = " ChoLong1004    "
#id.lower()  " cholong1004    "
print(id.lower().strip()) #"cholong1004"

#4-6. find() and rfine() : 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("o")) # Hell^o^ world
print(str.rfind("o")) # Hello w^o^rld
print(str.find("world"))
# 4-7. in() : 특정 문자열 포함하는지 확인 (True False)

# 문제
id = "cherry1004@gmail.com"
val = id[id.find("c"):id.find("4")+1]
#idx = id.find("@")
#val = id[:idx]
print(val)

url = "www.naver.com"
val = url.split(".")
print(val[1])