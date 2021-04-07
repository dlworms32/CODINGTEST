"""
    N-Queen

    공격 당하는 위치에 있는지 간단하게 판단하는 방법 생각하기
    출처: https://rebas.kr/761 [PROJECT REBAS]
"""
n, ans = int(input()), 0
a = [False]*n  # 세로 줄
b = [False]*(2*n-1)  # / 대각선
c = [False]*(2*n-1)  # \ 대각선

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)