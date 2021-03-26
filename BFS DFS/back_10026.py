from collections import deque
import copy

## R = 1, G = 2, B = 3 visited = 4
## R, G = 2, B = 3 visited = 4


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, n, x, y, color):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 4

    while queue:

        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == color:
                graph[nx][ny] = 4
                queue.append((nx, ny))


def cvt_map(graph, n,weakness=False):
    cvt_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'B':
                cvt_graph[i][j] = 3
            else:
                if graph[i][j] == 'R':
                    if weakness:
                        cvt_graph[i][j] = 2
                    else:
                        cvt_graph[i][j] = 1
                else:
                    cvt_graph[i][j] = 2

    return cvt_graph


if __name__ == '__main__':
    N = int(input())

    paint = [[]for _ in range(N)]

    for i in range(N):
        input_str = input()

        for char in input_str:
            paint[i].append(char)

    normal_map = cvt_map(paint, N, False)
    weekness_map = cvt_map(paint, N, True)

    normal_area = 0
    weekness_area = 0
    for color in range(1, 4):
        for x in range(N):
            for y in range(N):
                if normal_map[x][y] == color:
                    bfs(normal_map, N, x, y, color)
                    normal_area += 1

    for color in range(2, 4):
        for x in range(N):
            for y in range(N):
                if weekness_map[x][y] == color:
                    bfs(weekness_map, N, x, y, color)
                    weekness_area += 1

    print(normal_area, weekness_area)
