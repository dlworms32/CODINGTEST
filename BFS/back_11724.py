from collections import deque


def bfs(graph, table):
    num = 0
    for index in range(1, len(graph)):
        if not table[index]:
            queue = deque([index])
            table[index] = True
            # print('visit {}'.format(index))
            while queue:
                # print(queue)
                # print(table)
                c = queue.popleft()
                for next_node in graph[c]:
                    if not table[next_node]:
                        table[next_node] = True
                        # print('visit {} from {}'.format(c, index))
                        queue.append(next_node)
            num += 1
    return num


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(E):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)
# print(graph)
print(bfs(graph, visited))