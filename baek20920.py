import sys
sys.stdin = open("baek20920.txt")


N, M = map(int, sys.stdin.readline().split())

# key: 문자, value 인덱스
chk_map = {}
"횟수, 길이, 문자"
res_arr = []

idx = 0
for i in range(0, N):
    cur = sys.stdin.readline().rstrip()

    cur_len = len(cur)
    # 길이 M 이상만
    if cur_len >= M:
        if cur in chk_map.keys():
            cur_idx = chk_map[cur]
            res_arr[cur_idx][0] += 1
        else:
            chk_map[cur] = idx
            idx += 1
            res_arr.append([1, cur_len, cur])

res_arr.sort(key=lambda x : (-x[0], -x[1], x[2]))

for i in range(0, len(res_arr)):
    print(res_arr[i][2])