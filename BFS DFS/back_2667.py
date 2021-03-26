"""
    단지 번호 붙이기
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def view_map(graph):
    for i in range(len(graph)):
        print(graph[i])
    print('------------------------------')


def bfs(graph, w, h, x, y):
    num = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2
    while queue:
        cx, cy = queue.popleft()
        graph[cx][cy] = 2
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx == w or ny == h:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                num += 1

    return num


if __name__ == '__main__':
    N = int(input())
    input_arr = []

    for i in range(N):
        input_str = input()
        input_arr.append([int(input_str[index]) for index in range(len(input_str))])

    num_arr = []

    for i in range(N):
        for j in range(N):
            if input_arr[i][j] == 1:
                rnum = bfs(input_arr, N, N, i, j)
                if rnum > 0:
                    num_arr.append(rnum)

    num_arr.sort()
    print(len(num_arr))
    for i in range(len(num_arr)):
        print(num_arr[i])