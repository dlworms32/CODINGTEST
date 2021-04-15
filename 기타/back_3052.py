"""
    1차원 배열
    나머지
"""

arr = [int(input()) for _ in range(10)]

result = [i % 42 for i in arr]

print(len(set(result)))