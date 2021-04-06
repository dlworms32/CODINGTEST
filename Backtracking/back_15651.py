"""
    N과 M (3)
"""
N, M = map(int, input().split())

num = [i for i in range(N + 1)]
visited = [False] * (N + 1)
arr = []


def dfs(c): 
    if c == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        arr.append(num[i])
        visited[i] = True

        dfs(c + 1)

        arr.pop()
        visited[i] = False

dfs(0)