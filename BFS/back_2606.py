"""
    바이러스
"""


from collections import deque


def bfs(arr, visit):
    queue = deque()
    queue.append(1)

    while queue:
        node = queue.popleft()
        visit[node] = True

        for i in arr[node]:
            if not visit[i]:
                queue.append(i)
    num = 0
    for i in visit:
        if visit[i]:
            num += 1
    return num - 1


if __name__ == '__main__':
    N = int(input())
    edge = int(input())

    graph = [[] for i in range(N + 1)]
    visited = [False for i in range(N + 1)]
    for i in range(edge):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(bfs(graph, visited))