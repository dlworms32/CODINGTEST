"""
    치킨 배달
"""
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken_pos = []
house_pos = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_pos.append((i, j))
        if city[i][j] == 1:
            house_pos.append((i, j))

list_com = list(combinations(chicken_pos, M))  # 치킨집 M개 선택한 경우의 수

results = []

for chicken in list_com:
    # print(chicken)
    dist_map = [[0] * N for _ in range(N)]
    for pos in chicken:
        c_x, c_y = pos
        dist_map[c_x][c_y] = -1
        for house in house_pos:
            h_x, h_y = house
            dist = abs(c_x - h_x) + abs(c_y - h_y)
            if dist_map[h_x][h_y] == 0:
                dist_map[h_x][h_y] = dist
            elif dist_map[h_x][h_y] > dist:
                dist_map[h_x][h_y] = dist

    result = 0
    for house in house_pos:
        h_x, h_y = house
        result += dist_map[h_x][h_y]
    results.append(result)
    # print(*dist_map, sep='\n')
    # print('-----------------------')

print(min(results))