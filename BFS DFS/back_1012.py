from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, H, W):
    num = 0
    for x in range(H):
        for y in range(W):
            if graph[x][y] == 1:
                queue = deque()
                queue.append((x, y))
                graph[x][y] = 2
                num += 1
                while queue:

                    mx, my = queue.popleft()

                    for i in range(4):
                        nx = mx + dx[i]
                        ny = my + dy[i]

                        if nx < 0 or ny < 0 or nx >= H or ny >= W:
                            continue

                        if graph[nx][ny] == 1:
                            graph[nx][ny] = 2
                            queue.append((nx, ny))

    return num


T = int(input())
result_list = []
for case in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    result_list.append(bfs(field, M, N))

for result in result_list:
    print(result)