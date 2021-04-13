"""
    이중 우선순위 큐
"""
import sys
import heapq

T = int(sys.stdin.readline())

for i in range(T):

    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    length = 0
    comds = [sys.stdin.readline().split() for _ in range(k)]

    cond = True  # True : max heap, False : min heap
    for comd in comds:
        if comd[0] == 'I':  # insert
            heapq.heappush(max_heap, 0 - int(comd[1]))
            heapq.heappush(min_heap, int(comd[1]))
            length += 1

        else:  # delete
            if length > 0:
                if comd[1] == '1':  # 최댓값 삭제
                    heapq.heappop(max_heap)
                    length -= 1

                else:  # 최솟값 삭제
                    heapq.heappop(min_heap)
                    length -= 1

    if length > 0:
        ops_max_heap = [0] * (len(max_heap))
        for i in range(len(max_heap)):
            ops_max_heap[i] = 0 - max_heap[i]

        union = list(set(ops_max_heap) & set(min_heap))

        print(max(union), min(union))

    else:
        print('EMPTY')