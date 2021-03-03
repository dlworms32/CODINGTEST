from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_area = 0


def bfs(graph, w, h):
    global max_area
    # print('before....')
    # for low in graph:
    #     print(low)
    # print('----------------------------')
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 2:
                queue = deque()
                queue.append((x, y))

                while queue:
                    pop_x, pop_y = queue.popleft()
                    for direct in range(4):
                        nx = pop_x + dx[direct]
                        ny = pop_y + dy[direct]
                        if nx < 0 or ny < 0 or nx >= h or ny >= w:
                            continue

                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 2
                            queue.append((nx, ny))
    # print('finally....')
    # for low in graph:
    #     print(low)
    # print('==========================')
    num = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 0:
                num += 1

    if num > max_area:
        max_area = num


def make_wall(map, w, h, count):
    if count == 3:
        bfs(copy.deepcopy(map), w, h)
        return

    for i in range(h):
        for j in range(w):
            if map[i][j] == 0:
                map[i][j] = 1
                make_wall(map, w, h, count + 1)
                map[i][j] = 0


if __name__ == '__main__':
    H, W = map(int, input().split())
    lab = []
    for i in range(H):
        input_str = input().split()
        lab.append([int(input_str[index]) for index in range(len(input_str))])

    for i in range(H):
        for j in range(W):
            if lab[i][j] == 0:
                lab_copy = copy.deepcopy(lab)
                lab_copy[i][j] = 1
                make_wall(lab_copy, W, H, 1)
                lab_copy[i][j] = 0

    print(max_area)