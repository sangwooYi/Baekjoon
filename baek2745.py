import sys
sys.stdin = open("baek2745.txt")

N, M = input().split()
M = int(M)

str_chr = ord("A")

chr_map = {}
for i in range(0, 36):
    if 0 <= i < 10:
        chr_map[str(i)] = i
    else:
        cur_chr = str_chr + i - 10
        chr_map[chr(cur_chr)] = i

ans = 0
for i in range(0, len(N)):
    alph = N[len(N)-1-i]
    ans += (chr_map[alph]*(M**i))
print(ans)