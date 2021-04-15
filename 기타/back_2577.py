"""
    1차원 배열
    숫자의 개수
"""

arr = [int(input()) for _ in range(3)]

result = arr[0] * arr[1] * arr[2]

nums = [0] * 10
for num in str(result):
    nums[int(num)] += 1

for i in nums:
    print(i)