"""
    1차원 배열
    OX 퀴즈
"""

N = int(input())

for i in range(N):
    case = input()

    count = 1
    score = 0
    for j in case:
        if j == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)