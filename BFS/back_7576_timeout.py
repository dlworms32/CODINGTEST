"""
    토마토

"""
from collections import deque
import copy

direct = ['위', '아래', '왼쪽', '오른쪽']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def view_map(graph):
    for i in range(len(graph)):
        print(graph[i])
    print('------------------------------')


def find_comp(graph, w, h, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        graph[cx][cy] = 2

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 1:
                return True

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
    return False


def check_end(graph, w, h):
    for i in range(w):
        for j in range(h):
            if 0 in graph[i]:
                return False
    return True


def calc_date(graph, w, h):
    date = 0

    while True:
        date += 1
        for x in range(w):
            for y in range(h):
                if graph[x][y] == date:
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or ny < 0 or nx >= w or ny >= h:
                            continue

                        if graph[nx][ny] == 0:
                            graph[nx][ny] = date + 1

        if check_end(graph, w, h):
            break

    return date


if __name__ == '__main__':
    N, M = map(int, input().split())
    tomato = []

    for i in range(M):
        input_ = input().split()
        tomato.append([int(i) for i in input_])

    cond1 = True
    for i in range(M):
        for j in range(N):
            if 0 in tomato[i]:  # 박스에 안익은 토마토가 있을 경우
                cond1 = False
                break

    if cond1:
        print(0)  # 모든 토마토 익음

    else:
        cond2 = True  # 초기 토마토가 익을 수 없다고 가정

        for i in range(M):
            for j in range(N):
                if tomato[i][j] == 0:  # 박스에 안익은 토마토가 있을 경우
                    if not find_comp(copy.deepcopy(tomato), M, N, i, j):
                        cond2 = False
                        break
        if cond2:
            print(calc_date(tomato, M, N))
        else:
            print(-1)
