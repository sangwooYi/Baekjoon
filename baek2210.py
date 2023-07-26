import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek2210.txt")


"""
왔던 칸 또 가도 됨.. ㅡㅡ?
"""

def dfs_check(row, col, cur_str):

    # 종료 조건
    if len(cur_str) == 6:
        if str not in chk_map.keys():
            chk_map[cur_str] = 1
        return

    for d in range(0, 4):
        next_row = row + dr[d]
        next_col = col + dc[d]

        if next_row < 0 or next_col < 0 or next_row >=5 or next_col >= 5:
            continue
        next_str = cur_str + str(MAP[next_row][next_col])
        dfs_check(next_row, next_col, next_str)

MAP = [0] * 5
for i in range(0, 5):
    MAP[i] = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

chk_map = {}
for r in range(0, 5):
    for c in range(0, 5):
        dfs_check(r, c, "")

print(len(chk_map))