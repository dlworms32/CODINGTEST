"""
    1차원 배열
    평균은 넘겠지
"""

C = int(input())

for i in range(C):
    inp = input().split()
    num = int(inp[0])
    arr = inp[1:]

    total = 0
    for score in arr:
        total += int(score)

    avg = total / num

    p = 0
    for score in arr:
        if int(score) > avg:
            p += 1

    print('%0.3f' % round(p / num * 100, 3),end='')
    print('%')