"""
    퇴사
    출처 : https://pacific-ocean.tistory.com/199
"""
import sys

N = int(sys.stdin.readline())

tasks = [0] * (N)
pays = [0] * (N)

dp = [0] * (N + 1)
for i in range(N):
    T, P = map(int, sys.stdin.readline().split())

    tasks[i] = T
    pays[i] = P

# 거꾸로 탐색
for i in range(N - 1, -1, -1):
    if tasks[i] + i > N:  # 현재 상담 일정의 소요기간이 가용 날짜보다 큰 경우
        dp[i] = dp[i + 1]  # 이전 값과 동일
    else:  # 현재 상담 일정을 취할 경우
        dp[i] = max(dp[i + 1], pays[i] + dp[i + tasks[i]])
        # 현재 상담 일정을 선택했을 때,
        # 현재 금액(pays[i])과 맨 뒷 일정을 수행했을 때의 최댓값(dp[i + tasks[i]])을 더해줌
        # 현재 상담 일정을 선택하지 않을 경우
        # 이전까지의 최댓값(dp[i + 1])과 비교

# 최댓값 출력
print(max(dp))