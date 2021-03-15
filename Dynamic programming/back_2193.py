"""
    이친수
"""

N = int(input())

output = [0] * 91

output[1] = 1
output[2] = 1
output[3] = 2

for i in range(4, N + 1):
    output[i] = output[i-1] + output[i-2]

print(output[N])