"""
    이중 우선순위 큐
"""
import sys
import heapq

T = int(sys.stdin.readline())

for i in range(T):

    k = int(sys.stdin.readline())

    exist_arr = [False] * 10000000
    num_arr = [0] * 10000000
    num = 0

    comds = [sys.stdin.readline().split() for _ in range(k)]

    for comd in comds:
        if comd[0] == 'I':  # insert
            if num == 0:
                num_arr[1] = int(comd[1])
                exist_arr[1] = True
                num += 1
            else:
                start_index = 1
                while True:
                    if num_arr[start_index] <= int(comd[1]):
                        start_index = (2 * start_index) + 1
                    else:
                        start_index = 2 * start_index

                    if not exist_arr[start_index]:
                        exist_arr[start_index] = True
                        num_arr[start_index] = int(comd[1])
                        break
                num += 1

        else:  # delete
            if num > 0:
                start_index = 1
                if comd[1] == '1':  # 최댓값 삭제

                    while True:
                        next_index = (start_index * 2) + 1
                        if not exist_arr[next_index]:  # 최댓값
                            exist_arr[start_index] = False
                            break
                        else:
                            start_index = next_index

                else:  # 최솟값 삭제
                    while True:
                        next_index = (start_index * 2)
                        if not exist_arr[next_index]:  # 최댓값
                            exist_arr[start_index] = False
                            break
                        else:
                            start_index = next_index
                num -= 1

    if num != 0:
        start_index = 1
        while True:
            next_index = (start_index * 2) + 1
            if not exist_arr[next_index]:  # 최댓값
                max_val = num_arr[start_index]
                break
            else:
                start_index = next_index

        start_index = 1
        while True:
            next_index = (start_index * 2)
            if not exist_arr[next_index]:  # 최댓값
                min_val = num_arr[start_index]
                break
            else:
                start_index = next_index

        print(max_val, min_val)

    else:
        print('EMPTY')

        # for i, ele in enumerate(exist_arr):
        #     if i > 20:
        #          break
        #     print(ele, end=' ')
        # print()
        #
        # for i, ele in enumerate(num_arr):
        #     if i > 20:
        #          break
        #     print(ele, end=' ')
        # print()