"""
    while 문
    더하기 싸이클
"""

N = int(input())

temp = N
count = 0
while True:
    a = temp // 10
    b = temp % 10

    p = a + b

    temp = int(str(temp % 10) + str(p % 10))

    count += 1

    if temp == N:
        break

print(count)