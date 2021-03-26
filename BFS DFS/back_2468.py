from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_area = 0


def bfs(graph, size, x, y):
    queue = deque()
    queue.append((x, y))

    graph[x][y] = False
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                continue

            if graph[nx][ny]:
                graph[nx][ny] = False
                queue.append((nx, ny))


if __name__ == '__main__':
    N = int(input())
    map_input = []
    for i in range(N):
        input_str = input().split()
        map_input.append([int(input_str[index]) for index in range(len(input_str))])

    max_ = max(max(map_input))
    min_ = min(min(map_input))

    for rain in range(min_, max_ + 1):
        mask = [[] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if map_input[i][j] > rain:
                    mask[i].append(True)
                else:
                    mask[i].append(False)

        area = 0
        for i in range(N):
            for j in range(N):
                if mask[i][j]:
                    bfs(mask, N, i, j)
                    area += 1
        if area > max_area:
            max_area = area
    if max_area == 0:
        max_area = 1
    print(max_area)