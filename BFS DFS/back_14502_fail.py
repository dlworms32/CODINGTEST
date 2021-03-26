from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_pos(num, h, w):
    if num == 0:
        return 0, 0
    else:
        return num // h, num % w


def bfs(graph, w, h):
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
    num = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 0:
                num += 1
    # print('finally....')
    # for low in graph:
    #     print(low)
    # print('----------------------------')
    return num


H, W = map(int, input().split())
lab = []
for i in range(H):
    input_str = input().split()
    lab.append([int(input_str[index]) for index in range(len(input_str))])


max_land = 0
for x in range(H * W):

    rx1, ry1 = get_pos(x, W, H)

    if lab[rx1][ry1] == 0:
        # labcopy[rx1][ry1] = 1
        for y in range(x, H * W):
            rx2, ry2 = get_pos(y, W, H)
            if lab[rx2][ry2] == 0:
                # labcopy[rx2][ry2] = 1
                for z in range(y, H * W):
                    rx3, ry3 = get_pos(z, W, H)
                    if lab[rx3][ry3] == 0:
                        labcopy = copy.deepcopy(lab)
                        labcopy[rx1][ry1] = 1
                        labcopy[rx2][ry2] = 1
                        labcopy[rx3][ry3] = 1

                        # print('new col {}, {}\n{}, {}\n{}, {}'.format(rx1, ry1, rx2, ry2, rx3, ry3))
                        #
                        # for low in labcopy:
                        #     print(low)
                        # print('----------------------------')
                        result = bfs(labcopy, W, H)

                        if result > max_land:
                            # print('new col {}, {}\n{}, {}\n{}, {}'.format(rx1, ry1, rx2, ry2, rx3, ry3))
                            # print('new maximum result {}'.format(result))
                            max_land = result

print(max_land)