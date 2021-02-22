"""
    DFS와 BFS


"""
from collections import deque


def bfs(graph, V, visited):
    queue = deque([V])
    visited[V] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    input_arr = [[] for _ in range(N + 1)]
    visit = [False for _ in range(N + 1)]
    for i in range(M):
        r, c = map(int, input().split())
        input_arr[r].append(c)
        input_arr[c].append(r)
        input_arr[r].sort()
        input_arr[c].sort()

    print(input_arr)
    dfs(input_arr, V, visit.copy())
    print()
    bfs(input_arr, V, visit.copy())