"""
squre_run: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('squre_run.txt')


def calc_min_length(x, y, w, h):
    min_x = 0
    min_y = 0
    result = 0
    if x >= w - x:
        min_x = w - x
    else:
        min_x = x
    if y >= h - y:
        min_y = h - y
    else:
        min_y = y
    if min_x >= min_y:
        return min_y
    else:
        return min_x


X, Y, W, H = map(int, input().split())

answer = calc_min_length(X, Y, W, H)
print(answer)