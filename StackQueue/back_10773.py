"""
    제로
"""
import sys

K = int(sys.stdin.readline())

stack = [0] * 100001
pointer = 0

for _ in range(K):
    num = int(sys.stdin.readline())

    if num == 0:
        pointer -= 1

    else:
        stack[pointer] = num
        pointer += 1

print(sum(stack[:pointer]))
