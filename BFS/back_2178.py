from collections import deque

direct_x = [-1, 1, 0, 0]
direct_y = [0, 0, -1, 1]


def find(graph, x, y, W, H):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dist_x = x + direct_x[i]
            dist_y = y + direct_y[i]

            if dist_x < 0 or dist_y < 0 or dist_x >= W or dist_y >= H:
                continue
            if graph[dist_x][dist_y] == 1:
                graph[dist_x][dist_y] = graph[x][y] + 1
                queue.append((dist_x, dist_y))

    return graph[W - 1][H -1]


if __name__ == '__main__':
    N, M= map(int, input().split())
    maze = []

    for i in range(N):
        input_str = input()
        maze.append([int(input_str[index]) for index in range(len(input_str))])

    print(find(maze, 0, 0, N, M))