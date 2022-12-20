import sys
sys.stdin = open("baek2539.txt")


"""
left 값은 잘못 칠해진 행의 최댓값 (밑변에 붙여야 하므로)
right 값은 행의 최댓값부터 시작

mid = 현재 탐색하는 색종이의 크기 가 되며,

각 열마다 해당 열에 존재하는 잘못칠해진 숫자를 카운트

mid 크기로 주어진 색종이 숫자 이하로 해결 되면 다음 탐색범위를 더 줄인다. (right = mid)
더 많이 필요하면 다음 탐색범위를 더 키운다 (left = mid+1)

lower bound!  (처음 유효한 범위가 나오는 위치를 찾는것 즉, 유효한 탐색범위의 가장 작은 위치가 어디인질 찾는 것) 
"""

R, C = map(int, input().split())
N = int(input())
M = int(input())

# 특정 열에 잘못칠해진 칸이 몇개있는지 체크
wrong_dict = {}

# 색종이 탐색 left값 설정을 위함
max_row = 0
# 시작 열 위치를 찾기 위함
min_col = 987654321

for i in range(0, M):
    #행 열
    a, b = map(int, input().split())
    max_row = max(max_row, a)
    min_col = min(min_col, b)
    if b in wrong_dict.keys():
        wrong_dict[b] += 1
    else:
        wrong_dict[b] = 1


wrong_list = list(wrong_dict.keys())
wrong_list.sort()
left = max_row
right = C+1

while left < right:

    mid = (left+right)//2

    start_col = min_col
    idx = 0
    origami_cnt = 1
    
    col = start_col
    # 틀린 칸을 다 칠할 떄까지
    while idx < len(wrong_list):
        
        for i in range(0, mid):
            now_col = col+i

            if now_col in wrong_dict.keys():
                idx += 1
        if idx < len(wrong_list):
            col = wrong_list[idx]
            origami_cnt += 1
    
    # 다음 탐색범위 줄인다. (N개 충족이 되어도 다음범위를 더 줄여본다)
    if origami_cnt <= N:
        right = mid
    # 다음 탐색범위 키운다.
    else:
        left = mid+1
print(left)