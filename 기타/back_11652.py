"""
    카드
"""
import sys

N = int(sys.stdin.readline())

num_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

num_list = [(num_dict[key], key) for key in num_dict.keys()]
# 람다식으로 첫 번째 정렬기준과 두 번째 정렬기준을 명시
num_list = sorted(num_list, key=lambda x: (x[0], -x[1]), reverse=True)

print(num_list[0][1])