import sys
sys.stdin = open("baek3135.txt")

A, B = map(int, input().split())

N = int(input())
min_cnt = abs(A-B)

for i in range(0, N):
    cur = int(input())

    cur_cnt = abs(B-cur)+1
    min_cnt = min(min_cnt, cur_cnt)
print(min_cnt)