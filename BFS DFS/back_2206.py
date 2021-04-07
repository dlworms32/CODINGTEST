"""
    벽 부수고 이동하기

    출처 :https://yuuj.tistory.com/94
"""
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())

arr = [[int(j) for j in sys.stdin.readline().strip()] for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

if N == M == 1 and arr[0][0] == 0:
    print(1)
else:
    flag = 0
    while queue:
        cx, cy, before = queue.popleft()  # cx, cy 현재 위치 before 벽을 부순적이 있는지
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[before][nx][ny] == 0:
                if arr[nx][ny] == 1 and before == 0:  # 다음 위치가 벽이고, 벽을 부수지 않았을 경우
                    visited[1][nx][ny] = visited[0][cx][cy] + 1
                    queue.append((nx, ny, 1))

                elif arr[nx][ny] == 0:  # 길인 경우
                    visited[before][nx][ny] = visited[before][cx][cy] + 1
                    queue.append((nx, ny, before))

                if nx == N - 1 and ny == M - 1:  # 도착
                    print(visited[before][nx][ny])
                    flag = 1

            if flag == 1:
                break
    if flag == 0:
        print(-1)