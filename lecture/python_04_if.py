# 조건문(condition) : if~elif~else
# - 특정조건을 만족하는 경우 수행할 작업에 사용
# - 모든 조건은 boolean으로 표현 됨
# - 조건문의 경우 if, elif, else 블록 내 들여쓰기
# - 모든 블록문의 시작점의 마지막 : (콜론, colon) 추가

# JAVA & C
# if (조건문1) {
#   code
# } else if (조건문2) {
#   code
# } else if (조건문3) {
#   code
# } else {
#   code
# }

# Python
# if 조건문1:
#   code
# elif 조건문2:
#   code
# elif 조건문3:
#   code
# else
#   code
#

# if 조건문1:
#   code
# if 조건문2:
#   code
# if 조건문3:
#   code

# if문을 활용한 조합식
# 1. if
# 2. if~else
# 3. if~elif~elif
# 4. if~elif~else

# 논리 연산자(AND, OR, NOT)
# 1. AND
# 조건1 조건2 결과
# F and F     F
# T and F     F
# F and T     F
# T and T     T

# 2. OR
# F and F     F
# T and F     T
# F and T     T
# T and T     T

# 3. NOT
# F -> T
# T -> F

# A, B, C, D, F로 계산하는 프로그램
# 4.1~4.5 : A
# 3.6~4.0 : B
# 3.1~3.5 : C
# 2.6~3.0 : D
# 2.5 이하 : F

score = 4.2 # 총 학점 0.0~4.5
'''
if 4.5>=score>4.0:
    print("A")
elif 4.0>=score>3.5:
    print("B")
elif 3.5>=score>3.0:
    print("C")
else:
    print("F")
'''
if 4.5>= score >=0.0:
    if score>4.0:
        print("A")
    elif score>3.5:
        print("B")
    elif score>3.0:
        print("C")
    else:
        print("F")
else:


# Quiz

from datetime import datetime
now = datetime.today().year

# input() : 키보드로 값을 입력, String(문자열)
born = int(input("태어난 년도: "))

age = born - now+1

if 26 >= age >= 20:
    print("대학생")
elif age >= 17:
    print("고등학생")
elif age >= 16:
    print("중학생")
elif 13 >= age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")



a && b
b || a












