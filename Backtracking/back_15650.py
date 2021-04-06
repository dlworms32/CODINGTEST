"""
    N과 M (2)
"""
N, M = map(int, input().split())

num = [i for i in range(N + 1)]
visited = [False] * (N + 1)
arr = []


def dfs(c, idx):  # 이전 인덱스 이후부터 진행 -> 큰 수만 고려함
    if c == M:
        print(*arr)
        return

    for i in range(idx, N + 1):
        if visited[i]:
            continue

        arr.append(num[i])
        visited[i] = True

        dfs(c + 1, i + 1)

        arr.pop()
        visited[i] = False

dfs(0, 1)