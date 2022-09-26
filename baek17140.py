import sys
sys.stdin = open("baek17140.txt")

"""
현재 행 갯수 >= 열 갯수면 R 연산 -> 모든 행에대해 시행
현재 행 갯수 < 열 갯수면 C 연산 -> 모든 열에 대해 시행

연산 방법은 현재 탐색하는 행 or 열의 각각 숫자 등장 횟수를 체크
-> 그 후 등장 횟수, 해당 숫자 오름차순으로 정렬하여 
   해당 행에 다시 박아 넣는다.

ex) 
1 2 1   -> (2, 1), (1, 2)   // 등장횟수 오름차순이 더 우선 순위    
2 1 3   -> (1, 1), (2, 1), (3, 1)
3 3 3   -> (3, 3)

행 3 >= 열 3 이므로 R 연산이 위와같이 진행되며 그 다음 배열은
2 1 1 2 0 0
1 1 2 1 3 1 
3 3 0 0 0 0 
위와 같이 된다! 그다음은 행 3 < 열 6 이므로 C 연산이 진행 

이를 계속 반복해서 A[r][c]의 값이 k 가 되기위한 최소 시간을 출력

전략은
100*100 이차원 리스틀를 선언후
실제 데이터가 들어있는 최대 행 / 열 값을 따져가며
연산 시행하는 전략으로
"""

# 한 줄 계산해서 새로운 배열 반환 
def operByLine(arr):
    cnt_dict = {}
    for i in range(0, len(arr)):
        if arr[i] == 0:
            continue
        if arr[i] in cnt_dict.keys():
            cnt_dict[arr[i]] += 1
        else:
            cnt_dict[arr[i]] = 1
    tmp_arr = [0] * len(cnt_dict.keys())

    idx = 0
    for key in cnt_dict:
        # 등장 숫자, 숫자 등장 횟수
        tmp_arr[idx] = (key, cnt_dict[key])
        idx += 1
    # 등장 횟수, 등장 숫자 오름차순, 정렬 기준부분을 [x[1], x[0]] 으로 쓰던 (x[1], x[0])으로 쓰던 잘 동작함
    tmp_arr.sort(key=lambda x : (x[1], x[0]))
    new_arr = [0]*len(tmp_arr)*2
    idx = 0
    for i in range(0, len(tmp_arr)):
        num, cnt = tmp_arr[i]
        new_arr[idx] = num
        new_arr[idx+1] = cnt
        idx += 2
    return new_arr

def operR(arr):

    next_col_len = 0
    for i in range(0, row_len):
        tmp_arr = [0] * col_len
        for j in range(0, col_len):
            tmp_arr[j] = arr[i][j]
            # 다음 대입을 위해 미리 초기화
            arr[i][j] = 0
        res_oper = operByLine(tmp_arr)
        # 결과 대입
        for j in range(0, len(res_oper)):
            arr[i][j] = res_oper[j]
        next_col_len = max(next_col_len, len(res_oper))
    return next_col_len

def operC(arr):
    next_row_len = 0
    for j in range(0, col_len):
        tmp_arr = [0] * row_len
        for i in range(0, row_len):
            tmp_arr[i] = arr[i][j]
            arr[i][j] = 0
        res_oper = operByLine(tmp_arr)
        for i in range(0, len(res_oper)):
            arr[i][j] = res_oper[i]
        next_row_len = max(next_row_len, len(res_oper))
    return next_row_len


r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(0, 100)]
for i in range(0, 3):
    temp = list(map(int, input().split()))
    for j in range(0, 3):
        arr[i][j] = temp[j]

# 현재 데이터가 저장된 최대 행 / 열 값을 계속 갱신하며 진행
row_len = 3
col_len = 3
time = 0
while time <= 100:
    # 위에서 주어진 행, 열값은 1부터 시작
    if arr[r-1][c-1] == k:
        break
    
    # R 연산
    if row_len >= col_len:
        # R연산에서 행 수는 유지, 열 수가 바뀜
        next_col_len = operR(arr)
        col_len = next_col_len
    # C 연산
    else:
        next_row_len = operC(arr)
        row_len = next_row_len
    time += 1

# 100회 안에 연산 실패
if time > 100:
    time = -1
print(time)

