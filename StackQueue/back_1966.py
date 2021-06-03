"""
    프린터 큐
"""
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    prior = list(map(int, sys.stdin.readline().split()))

    # p : 중요도, i : 입력된 인쇄 순서
    queue = deque([(p, i) for i, p in enumerate(prior)])

    count = 1  # 몇 번째로 인쇄되는지
    while True:
        max_index = 0
        max_prior = queue[0][0]

        # 1 : 현재 출력할 문서(큐의 맨 앞)의 중요도보다 높은 중요도를 가진 문서를 찾음
        if max_prior != max(queue)[0]:
            max_prior = max(queue)[0]
            for index, element in enumerate(queue):
                q_prior, q_index = element
                if max_prior == q_prior:
                    max_index = index
                    break

        # 2 : if 현재 출력할 문서보다 높은 중요도를 가진 문서가 존재할 경우:
        # 인덱스 만큼 큐 rotation
        queue.rotate(-max_index)

        # 프린터 출력
        output_docs = queue.popleft()
        # 3: if M번째 인덱스를 가진 문서:
        #           count 출력
        #     else:
        #           count += 1
        if output_docs[1] == M:
            print(count)
            break
        else:
            count += 1