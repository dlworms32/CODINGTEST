"""
    더하기 싸이클
"""

N = int(input())

init = 0
if N < 10:  # 두자리 수로 만들기
    init = int(str(N) + '0')
else:
    init = N

count = 0

while True:
    