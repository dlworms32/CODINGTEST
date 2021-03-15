"""
    2×n 타일링 2
"""

N = int(input())

output = [0] * 1001

output[1] = 1
output[2] = 3

for i in range(3, N + 1):
    output[i] = ((output[i - 2] * 2) + output[i - 1]) % 10007

print(output[N])