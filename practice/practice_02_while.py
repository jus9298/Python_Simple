# Q
# # 1. 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료
# pw = 1234
#
# i = 0
# while True:
#     a = int(input("암호: "))
#     if pw == a:
#         print("welcome")
#         break
#     else:
#         print("wrong answer")
#         i += 1
#         if i==3:
#             print("프로그램 종료")
#             break

# 2. 1~100까지 더해서 총합계산
sum = 0
i = 1
while True:
    sum += i
    i += 1
    if i==101:
        break
print(sum)
