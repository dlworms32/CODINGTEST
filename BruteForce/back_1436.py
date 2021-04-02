"""
    영화감독 숌
"""

import sys

N = int(sys.stdin.readline())

rank = 0
num = 666

while True:
    s = str(num)

    if s.find('666') != -1:
        rank += 1

    if N == rank:
        print(num)
        exit(0)
    num += 1