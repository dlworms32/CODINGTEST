"""
    분해합
"""
import sys

result = int(sys.stdin.readline())

r_list = []
for num in range(1, result + 1):
    s = str(num)
    sum = 0
    for i in s:
        sum += int(i)

    div_sum = sum + num
    if div_sum == result:
        r_list.append(num)

if len(r_list) > 0:
    print(min(r_list))
else:
    print(0)