# 예외 처리
# ** 예외(Exception)
#     - 프로그램을 개발하면서 예상하지 못한 상황
#     ex) 사용자 입력 오류
#     - 예외처리를 사용하면 프로그램이 종료 x
#     입력 오류 -> 프로그램 종료(Error)
#     - 데이터베이스 또는 파일시스템 사용할 때는 반드시 예외처리!!
#
#     ** 예외 종류
#     1. 예측 가능한 예외
#         -발생 여부를 개발자가 사전에 인지
#     2. 예측 불가능한 예외
#         -서버에서 데이터 받기(서버 화재발생으로 서버 종료)

# 정부 통합 데이터 센터 #파견..

# 예외 기본 문법
# try:
#     예외가 발생할수도 있는 코드
# except 예외 타입:
#     예외 발생시 실행되는 코드(예외처리)
# else:
#     예외가 발생하지 않은 경우 실행되는 코드
# finally:
#     무조건 실행되는 코드(예외 발생여부 상관없음)
#     (대부분 자원 해제에 사용)
# 자원해제
# 가정: 종합정보시스템(동시접속 2,000명)
    - 학생1 <-> 종합졍보시스템(Connected)
    - 학생2 <-> 종합졍보시스템(Connected)

from import HTTPError

try:
    html = urlopen("http://www.naver.com")
except HTTPError as e:
    print(e)
else:
    print("자원해제")