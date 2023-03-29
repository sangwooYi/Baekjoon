import sys
sys.stdin = open("baek16139.txt")


S = sys.stdin.readline()
Q = int(sys.stdin.readline())


alph_dict = {}

a_code = ord("a")
z_code = ord("z")
# 최대 20만 * 26
for i in range(a_code, z_code+1):
    alph_dict[chr(i)] = [0] * len(S)


for i in range(0, len(S)):
    now_char = S[i]
    for j in range(a_code, z_code+1):
        tmp_char = chr(j)
        if tmp_char == now_char:
            if i == 0:
                alph_dict[tmp_char][0] = 1
            else:
                alph_dict[tmp_char][i] = alph_dict[tmp_char][i-1]+1
        else:
            if i > 0:
                alph_dict[tmp_char][i] = alph_dict[tmp_char][i-1]

for i in range(0, Q):
    alph, start, end = sys.stdin.readline().split()
    start = int(start)
    end = int(end)

    ans = alph_dict[alph][end]
    if start > 0:
        ans -= alph_dict[alph][start-1]
    print(ans)