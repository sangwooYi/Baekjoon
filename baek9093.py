import sys
sys.stdin = open("baek9093.txt")

T = int(input())

for tc in range(0, T):
    tmp = list(input().split())
    
    for i in range(0, len(tmp)):
        cur = tmp[i]
        rev_str = ''
        for j in range(len(cur)-1, -1, -1):
            rev_str += cur[j]
        tmp[i] = rev_str
    ans = " ".join(tmp)
    print(ans)