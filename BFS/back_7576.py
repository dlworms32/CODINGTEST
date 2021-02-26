from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(map, N, M, pos):
    queue = deque()
    pos_date = 0

    for p in pos:
        queue.append(p)

    while queue:
        x, y = queue.popleft()
        pos_date = map[x][y]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if map[nx][ny] == 0:
                map[nx][ny] = pos_date + 1
                queue.append((nx, ny))

    for i in range(M):
        for j in range(N):
            if map[i][j] == 0:
                return -1

    return pos_date - 1


if __name__ == '__main__':
    N, M = map(int, input().split())
    tomato = []

    for i in range(M):
        input_ = input().split()
        tomato.append([int(i) for i in input_])

    t_pos = []
    for i in range(M):
        for j in range(N):
            if tomato[i][j] == 1:
                t_pos.append((i, j))

    print(bfs(tomato, N, M, t_pos))

