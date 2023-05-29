import sys
sys.stdin = open("baek1712.txt")

A, B, C = map(int, input().split())

if C == B:
    ans = -1
else:
    bep_cnt = A/(C-B) 

    if bep_cnt <= 0:
        ans = -1
    else:
        ans = int(bep_cnt)+1
print(ans)