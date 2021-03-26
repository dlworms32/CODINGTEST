from collections import deque


def bfs(graph, pos1, pos2):
    queue = deque()
    queue.append(pos1)
    graph[pos1] = 1
    answer = 0
    while queue:
        current_pos = queue.popleft()
        # print('현재 위치 {}, 값 {}'.format(current_pos, graph[current_pos]))
        # print('==============================================')
        # print('index')
        # print(' 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, ^')
        # print(graph)

        if current_pos == pos2:
            # print('종료')
            # print('==============================================')
            # print('index')
            # print(' 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, ^')
            # print(graph)
            answer = graph[current_pos] - 1
            break

        before_pos = current_pos - 1
        next_pos = current_pos + 1
        double_pos = current_pos * 2

        # if before_pos == pos2 or next_pos == pos2 or double_pos == pos2:
        #     return graph[current_pos] - 1

        if 0 <= before_pos < 100001:
            if graph[before_pos] == 0:
                graph[before_pos] = graph[current_pos] + 1
                queue.append(before_pos)

        if 0 <= next_pos < 100001:
            if graph[next_pos] == 0:
                graph[next_pos] = graph[current_pos] + 1
                queue.append(next_pos)

        if 0 <= double_pos < 100001:
            if graph[double_pos] == 0:
                graph[double_pos] = graph[current_pos] + 1
                queue.append(double_pos)

    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())

    graph = [0 for _ in range(100001)]
    print(bfs(graph, N, K))