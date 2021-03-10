"""
    1로 만들기
"""

N = int(input())

d = [0] * 1000001

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1  # 일단 1칸 증가했다고 가정

    if i % 2 == 0:  # 2로 나눠 떨어질 경우
        d[i] = min(d[i], d[i // 2] + 1)  # 1/2 번째 인덱스의 값과 현재 값 비교,
                                         # 더 작은 값으로 변경
    if i % 3 == 0:  # 3으로 나눠 떨어질 경우
        d[i] = min(d[i], d[i // 3] + 1)  # 1/3 번째 인덱스의 값과 현재 값 비교,
                                         # 더 작은 값으로 변경
print(d[N])