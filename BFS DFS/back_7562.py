from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(graph, N, x, y, dest_x, dest_y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        cx, cy = queue.popleft()
        if cx == dest_x and cy == dest_y:
            return graph[cx][cy]

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[cx][cy] + 1
                queue.append((nx, ny))


if __name__ == '__main__':
    num = int(input())

    for case in range(num):
        N = int(input())

        graph = [[0 for j in range(N)] for i in range(N)]

        n_x, n_y = map(int, input().split())
        d_x, d_y = map(int, input().split())

        print(bfs(graph, N, n_x, n_y, d_x, d_y))

