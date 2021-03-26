"""
    이분 그래프
"""

import sys
from collections import deque


def bfs(g, v, c, visit):
    queue = deque()
    queue.append(v)
    c[v] = 1  # 맨 처음 1로 칠함
    visit[v] = True  # 방문 완료
    while queue:
        vertex = queue.popleft()  # 뽑음
        for i in g[vertex]:  # 인접 노드 방문
            if not visit[i]:   # 방문하지 않은 경우
                queue.append(i)  # 큐에 삽입
                if color[vertex] == 1:  # 현재 노드의 색이 1인 경우
                    color[i] = 2  # 2로 칠함
                elif color[vertex] == 2:  # 현재 노드의 색이 2인 경우
                    color[i] = 1  # 1로 칠함
                visit[i] = True  # 방문 완료
            else:  # 방문한 경우
                if color[vertex] == color[i]:  # 색깔이 같은 경우
                    return False  # 이분 그래프가 아님
    return True  # 안걸리면 이분 그래프


if __name__ == '__main__':
    K = int(sys.stdin.readline())

    for i in range(K):
        V, E = map(int, sys.stdin.readline().split())
        graph = [[] for num in range(V + 1)]
        color = [0] * (V + 1)
        visited = [False] * (V + 1)
        for _ in range(E):
            x, y = map(int, sys.stdin.readline().split())
            graph[x].append(y)
            graph[y].append(x)

        result = True
        while True:
            if False in visited[1:]:  # 모든 노드 방문 확인
                if not bfs(graph, visited[1:].index(False) + 1, color, visited):
                    result = False
                    break
            else:
                break
        if result:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')