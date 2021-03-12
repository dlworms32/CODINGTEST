N = int(input())

paint = []  # 페인트 비용

value = [[0] * 3 for _ in range(N)]  # 총 비용


for i in range(N):
    r, g, b = map(int, input().split())
    paint.append([r, g, b])

for i in range(N):
    if i == 0:
        value[i] = paint[i]
    else:
        value[i][0] = paint[i][0] + min(value[i - 1][1], value[i - 1][2])
        value[i][1] = paint[i][1] + min(value[i - 1][0], value[i - 1][2])
        value[i][2] = paint[i][2] + min(value[i - 1][0], value[i - 1][1])


print(min(min(value[N-1][0], value[N-1][1]), value[N-1][2]))