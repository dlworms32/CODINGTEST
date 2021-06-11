"""
    괄호
"""
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().strip()
    flag = False
    counting = 0
    for char in string:
        if char == '(':
            counting += 1
        elif char == ')':
            counting -= 1

        if counting < 0:
            flag = True
            break
    if counting != 0 or flag:
        print("NO")
    else:
        print("YES")