"""
    시간초과 뜸
"""
import sys, heapq

T = int(sys.stdin.readline())

for i in range(T):

    k = int(sys.stdin.readline())
    heap = []

    comds = [sys.stdin.readline().split() for _ in range(k)]

    for comd in comds:
        if comd[0] == 'I':  # insert
            heapq.heappush(heap, int(comd[1]))

        else:  # delete
            if len(heap) > 0:
                if comd[1] == '1':
                    heap.remove(max(heap))
                else:
                    heapq.heappop(heap)

    if len(heap) > 0:
        print(max(heap), heap[0])
    else:
        print('EMPTY')