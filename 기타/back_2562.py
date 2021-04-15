"""
    1차원 배열
    최댓값
"""

arr = [int(input()) for _ in range(9)]

print(max(arr))
print(arr.index(max(arr)) + 1)