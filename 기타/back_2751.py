"""
    정렬
    수 정렬하기
"""

import sys

N = int(sys.stdin.readline())

arr = [0] * N

for i in range(N):
    arr[i] = int(sys.stdin.readline())


for i in sorted(arr):
    sys.stdout.writelines("{}\n".format(i))