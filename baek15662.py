import sys
sys.stdin = open("baek15662.txt")

"""
톱니바퀴의 1은 S극, 0은 N극

회전 방향에서는 1은 시계방향 -> , -1은 반시계방향 <-

맞물리는 톱니의 인덱스는 2와 6

회전하는 톱니 기준으로 왼쪽 / 오른쪽을 순회하며 돌아가는 톱니 체크
(중간에 안돌아가는애 생기면 종료하면 된다.)
=> 그 후 돌아가는 톱니만 회전시킴
"""

def rotate_clockwise(arr):
    tmp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = tmp

def rotate_counter_clockwise(arr):
    tmp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = tmp

N = int(input())
cogwheels = [0] * N
for i in range(0, N):
    cogwheels[i] = list(map(int, input()))

K = int(input())
for i in range(0, K):
    a, b = map(int, input().split())
    a -= 1
    
    # 안움직이면 0 , 움직이면 1과 -1을 저장 (1이 시계, -1이 반시계)
    is_rotate = [0] * N
    is_rotate[a] = b

    # 왼쪽 순회 / 현재 인덱스 2과, 이전톱니 인덱스6 를 비교
    tmp_rotate = b
    for i in range(a-1, -1, -1):
        # 돌아감
        if cogwheels[i][2] != cogwheels[i+1][6]:
            tmp_rotate *= -1
            is_rotate[i] = tmp_rotate
        else:
            break
    tmp_rotate = b
    # 오른쪽 순회 / 현재 인덱스 6와 이전톱니 인덱스 6을 비교
    for i in range(a+1, N):
        if cogwheels[i][6] != cogwheels[i-1][2]:
            tmp_rotate *= -1
            is_rotate[i] = tmp_rotate
        else:
            break
    for i in range(0, N):
        if is_rotate[i] == 1:
            rotate_clockwise(cogwheels[i])
        elif is_rotate[i] == -1:
            rotate_counter_clockwise(cogwheels[i])

cnt = 0
for i in range(0, N):
    if cogwheels[i][0]:
        cnt += 1
print(cnt)