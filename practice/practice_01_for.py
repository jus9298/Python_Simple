# Q
# 1. 사용자가 입력한 단수를 출력하는 코드

# n = int(input("단을 입력하시오: "))
# for i in range(1,10,1):
#     print("%d * %d = %d" %(n, i, n*i))

# 2. 2단부터 9단까지 출력(중첩 for문)
# for i in range(2, 10, 1):
#     for j in range(1, 10, 1):
#         print("%d * %d = %d" % (i, j, i * j))

# 3. list a의 평균값을 계산하시오.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a길이 => len(a)
sum = 0
for i in a:
    sum += i
print("a의 평균: %.2f" %(sum/len(a)))
# round(값, 자리수) : 자리수만큼 반올림
#print(rount(x, 2)

# 4. list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]
for i in b:
    if i < int(min):
        min = i
    else:
        continue
print(f"최소값: {min}")

# 5. list c에서 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]
min = c[0]
max = c[0]

for i in c:
    if i < int(min):
        min = i
    elif i > max:
        max = i
    else:
        continue

print(f"최소값: {min}, 최대값:{max}")