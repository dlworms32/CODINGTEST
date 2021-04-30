"""
    절댓값 힙
"""
import sys
import heapq

N = int(sys.stdin.readline())
heap = []

comds = [int(sys.stdin.readline()) for _ in range(N)]

for x in comds:
    if x == 0:  # 가장 작은 값 출력 후, 제거
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))