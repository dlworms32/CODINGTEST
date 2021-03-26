from collections import deque


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(graph, w, h, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2

    while queue:
        cx, cy = queue.popleft()

        for direct in range(8):
            nx = cx + dx[direct]
            ny = cy + dy[direct]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx, ny))


if __name__ == '__main__':
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        map_input = []
        for i in range(H):
            input_str = input().split()
            map_input.append([int(input_str[index]) for index in range(len(input_str))])

        num_island = 0

        for i in range(H):
            for j in range(W):
                if map_input[i][j] == 1:
                    bfs(map_input, W, H, i, j)
                    num_island += 1

        print(num_island)