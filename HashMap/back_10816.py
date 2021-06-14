"""
    숫자 카드 2
"""
import sys
from collections import Counter
N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

card_dict = Counter(num_list)

M = int(sys.stdin.readline())

output_list = list(map(int, sys.stdin.readline().split()))

card_count = [0] * M

for i in range(M):
    card_count[i] = card_dict[output_list[i]]

print(*card_count, sep=' ')

