"""
    1차원 배열
    평균
"""


N = int(input())

arr = input().split()

arr = [int(i) for i in arr]

max_val = max(arr)

new_score = [score/max_val * 100 for score in arr]

print(sum(new_score) / N)
