"""
    N과 M (4)
"""

N, M = map(int, input().split())

num = [i for i in range(N + 1)]
visited = [False] * (N + 1)
arr = []


def dfs(c, n):  # 이전에 추가한 값을 기준
    if c == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if i >= n:  # 이전 값보다 크거나 같을 경우 추가
            arr.append(num[i])
            visited[i] = True

            dfs(c + 1, num[i])

            arr.pop()
            visited[i] = False

dfs(0, 0)