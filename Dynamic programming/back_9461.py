"""
    파도반 수열
"""

result = [0] * 101

result[1] = 1
result[2] = 1
result[3] = 1
result[4] = 2
result[5] = 2
result[6] = 3

for i in range(7, 101):
    result[i] = result[i - 5] + result[i - 1]

T = int(input())

input_list = []
for i in range(T):
    input_list.append(int(input()))

for i in input_list:
    print(result[i])