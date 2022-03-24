import sys
sys.stdin = open("baek2675.txt")


T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    ans = ""
    strings = list(S)
    for i in range(0, len(strings)):
        now = strings[i]
        for j in range(0, int(R)):
            ans += now
    print(ans)