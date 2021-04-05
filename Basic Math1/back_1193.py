"""
    분수찾기
"""

X = int(input())

if X == 1:
    print('1/1')
    exit(0)

row = 1
step = 1
while True:
    if step > X:
        break
    step += row
    row += 1
if row % 2 == 1:  # 홀수
    d = step - X
    m = row - d
    print('{}/{}'.format(m, d))
else:
    m = step - X
    d = row - m
    print('{}/{}'.format(m, d))