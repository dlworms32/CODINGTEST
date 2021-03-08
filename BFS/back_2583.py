from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, w, h, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2
    area = 1
    while queue:
        cx, cy = queue.popleft()
        graph[cx][cy] = 2

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if graph[nx][ny] == 0:
                area += 1
                graph[nx][ny] = 2
                queue.append((nx, ny))

    return area



if __name__ == '__main__':
    H, W, K = map(int, input().split())
    graph = []
    for i in range(H):
        graph.append([0 for _ in range(W)])

    for i in range(K):
        y1, x1, y2, x2 = map(int, input().split())
        x1 = H - x1
        x2 = H - x2

        for x in range(x2, x1):
            for y in range(y1, y2):
                graph[x][y] = 1

    num_area = 0
    total_area = []

    for i in range(H):
        for j in range(W):
            if graph[i][j] == 0:
                calc_area = bfs(graph, W, H, i, j)

                total_area.append(calc_area)
                num_area += 1

    for i in graph:
        print(i)

    total_area.sort()
    print(num_area)
    for area in total_area:
        print(area, end=' ')