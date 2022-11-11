import sys
sys.stdin = open("baek16927.txt")

"""
min(N, M)mode2 == 0 
따라서 안쪽으로 돌리는 배열중 한줄짜리가 나오는경우는 없다!
"""

def rotate_anticlockwise():
    row_len = N
    col_len = M

    cnt = 0
    # 둘중에 하나라도 길이가 1이되면 종료 (회전 불가)
    while row_len > 1 and col_len > 1:
        lu = arr[cnt][cnt]
        ru = arr[cnt][M-1-cnt]
        ld = arr[N-1-cnt][cnt]
        rd = arr[N-1-cnt][M-1-cnt]
        # 위
        for i in range(1+cnt, M-1-cnt):
            arr[cnt][i-1] = arr[cnt][i]
        # 아래
        for i in range(M-2-cnt, cnt, -1):
            arr[N-1-cnt][i+1] = arr[N-1-cnt][i]
        # 좌
        for i in range(N-2-cnt, cnt, -1):
            arr[i+1][cnt] = arr[i][cnt]
        # 우
        for i in range(1+cnt, N-1-cnt):
            arr[i-1][M-1-cnt] = arr[i][M-1-cnt]
        arr[cnt+1][cnt] = lu
        arr[cnt][M-2-cnt] = ru
        arr[N-1-cnt][cnt+1] = ld
        arr[N-2-cnt][M-1-cnt] = rd
        cnt += 1
        row_len -= 2
        col_len -= 2

def deep_copy(arr):

    tmp_arr = [[0] * M for _ in range(0, N)]

    for i in range(0, N):
        for j in range(0, M):
            tmp_arr[i][j] = arr[i][j]
    return tmp_arr

N, M, R = map(int, input().split())
arr = [0] * N
for i in range(0, N):
    arr[i] = list(map(int, input().split()))


cycle_num = (N+M-2)*2
rotate_save = [0] * cycle_num

rotate_save[0] = deep_copy(arr)
for i in range(1, cycle_num):
    rotate_anticlockwise()
    rotate_save[i] = deep_copy(arr)


res_arr = [[0] * M for _ in range(0, N)]

cnt = min(N, M)//2

for i in range(0, cnt):
    row_len = N - i*2
    col_len = M - i*2
    # rotation 갯수는 sub 배열마다 다르다는게 함정!
    cycle_count = (row_len+col_len-2)*2

    real_R = R %cycle_count
    tmp_res = rotate_save[real_R]

    for row in range(i, N-i):
        res_arr[row][i] = tmp_res[row][i]
        res_arr[row][M-1-i] = tmp_res[row][M-1-i]
    for col in range(i, M-i):
        res_arr[i][col] = tmp_res[i][col]
        res_arr[N-1-i][col] = tmp_res[N-1-i][col]
for i in range(0, N):
    print(" ".join(map(str, res_arr[i])))