import sys
sys.stdin = open("baek15686.txt")

"""
아이디어1.
모든 조합에 대해 구한다.
치킨거리는 그냥 |r1 - r2| + |c1-c2| 이 공식 활용!

13C6 해봤자 1700번정도.. 따라서 가능!
"""



def calc_path(c_arr, h_arr):
    INF = 98765
    res = [INF] * len(h_arr)
    for i in range(0, len(c_arr)):
        c_row, c_col = c_arr[i]
        for j in range(0, len(h_arr)):
            h_row, h_col = h_arr[j]
            path = abs(c_row-h_row) + abs(c_col-h_col)
            if res[j] > path:
                res[j] = path
    count = 0
    for i in range(0, len(res)):
        count += res[i]
    return count



# arr에는 치킨집 좌표가 저장 되어 있음
def comb(arr, h_list, visited, start, n, r, c):
    global min_path
    if r == 0:
        temp = [0] * c
        idx = 0
        for i in range(0, len(arr)):
            if visited[i]:
                temp[idx] = arr[i]
                idx += 1
        cnt = calc_path(temp, h_list)
        if min_path > cnt:
            min_path = cnt
        return
    
    for i in range(start, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, h_list, visited, i+1, n, r-1, c)
        visited[i] = False


N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

houses = []
chicks = []
min_path = 9876543
for i in range(0, N):
    for j in range(0, N):
        if MAP[i][j] == 1:
            houses.append((i, j))
        elif MAP[i][j] == 2:
            chicks.append((i, j))
check = [False] * len(chicks)
comb(chicks, houses, check, 0, len(chicks), M, M)
print(min_path)