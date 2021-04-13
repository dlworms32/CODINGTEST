"""
    이중 우선순위 큐
"""
import sys
import heapq

def minToMax(x):
    l = []
    for i in x:
        heapq.heappush(l, - i)
    return l

def maxToMin(x):
    l = []
    for i in x:
        heapq.heappush(l, - i)
    return l

T = int(sys.stdin.readline())

for i in range(T):

    k = int(sys.stdin.readline())
    heap = []

    comds = [sys.stdin.readline().split() for _ in range(k)]

    cond = True  # True : max heap, False : min heap
    for comd in comds:
        if comd[0] == 'I':  # insert
            if cond:  # 최대 힙
                heapq.heappush(heap, 0 - int(comd[1]))
            else:  # 최소 힙
                heapq.heappush(heap, int(comd[1]))

        else:  # delete
            if len(heap) > 0:
                if comd[1] == '1':  # 최댓값 삭제
                    if not cond:
                        heap = minToMax(heap)
                    heapq.heappop(heap)

                else:  # 최솟값 삭제
                    if cond:
                        heap = maxToMin(heap)
                    heapq.heappop(heap)

    if len(heap) > 0:
        if cond:
            print(0 - heapq.heappop(heap), end=' ')
            maxToMin(heap)
            print(heapq.heappop(heap))
        else:
            minVal_heap = heapq.heappop(heap)
            minToMax(heap)
            print(0 - heapq.heappop(heap), minVal_heap)

    else:
        print('EMPTY')