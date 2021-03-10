"""
    피보나치 함수
"""

T = int(input())

for i in range(T):
    N = int(input())

    dp = [] * 40

    dp_0 = [0] * 41
    dp_1 = [0] * 41

    dp_0[0] = 1
    dp_1[0] = 0

    dp_0[1] = 0
    dp_1[1] = 1
    for j in range(2, N + 1):
        dp_0[j] = dp_0[j - 2] + dp_0[j - 1]
        dp_1[j] = dp_1[j - 2] + dp_1[j - 1]

    print('{} {}'.format(dp_0[N], dp_1[N]))