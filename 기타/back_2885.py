"""
    알람시계
"""

h, m = map(int, input().split())

om = m - 45

if om < 0:
    oh = h - 1
    if oh < 0:
        print('{} {}'.format(24 + oh, 60 + om))
    else:
        print('{} {}'.format(oh, 60 + om))
else:
    print('{} {}'.format(h, om))