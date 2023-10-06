# while 반복문
# - 반복문 횟수를 모르는 경우
# - 조건이 만족 하는 동안 계속 반복
# - 조건 True -> 반복
# - 조건 False -> 반복 종료
# - while문의 조건을 True로
#   (이런 경우 반드시 if~break문과 함께 사용할 것)

# while 기본 문법
# while 조건:
#   실행문

a = list(range(1, 6)) # [1, 2, 3, 4, 5]
print(a)
i = 0
while i < len(a):
    print(a[i])
    i += 1