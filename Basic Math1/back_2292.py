"""
    벌집
"""

N = int(input())

if N == 1:
    print(1)
else:
    num = 1  # 통과 방 개수
    room = 1  # 방 번호
    before = 1  # 이전 경계 마지막 방 번호
    while True:
        room += (6 * num)

        if before < N <= room:
            break
        else:
            before = room
            num += 1
    print(num + 1)