import sys
sys.stdin = open("baek14499.txt")

"""
게임룰
1. 주사위를 매번 주어지는 방향에 따라 굴린다.
동 서 북 남
1  2  3  4
2. 주사위 굴린 이후에, 칸에 적힌 값이 0이면 주사위 바닥값이 칸에 복사,
   아니면 칸에 적힌 값이 주사위 바닥면에 복사
3. 만약 이동하려는 방향이 맵을 벗어나면 그냥 무시
4. 맵 안에 있다면, 굴린 이후, 윗면이 나타내는 값을 출력

Idea1.
매번 굴릴때마다 인덱스 매칭을 다시시켜준다!
아래는 굴릴때마다 현재 포인트에 오게 될 포인트값을 나타냄 
현재 위치   동  서  북  남  
   1       4    3   5  2
   2       2    2   1  6
   3       1    6   3   3
   4       6    1   4   4
   5       5    5   6   1
   6       3    4   2   5

아니 구현문제 풀때 잔실수좀 조심하자 ㅠㅠ
"""

def play_dice(arr, r, c, operations, x, y):

    # 동 서 북 남
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    # 초기 주사위 위치
    row = x
    col = y
    # 초기 주사위 값
    # 0이 항상 위, 5가 항상 아래
    dice = [0] * 6
    # 출력 용
    result = []
    for i in range(0, len(operations)):
        oper = operations[i]
        # 방향
        di = oper-1
        next_row = row + dr[di]
        next_col = col + dc[di]
        # 맵 밖으로 벗어났으면 아예 명령을 무시해야 한다.
        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
            continue
        # 맵 안으로는 들어오는 명령
        temp_dice = [0] * 6
        # 동 
        if oper == 1:
            temp_dice[0] = dice[3]
            temp_dice[5] = dice[2]
            temp_dice[1] = dice[1]
            temp_dice[4] = dice[4]
            temp_dice[2] = dice[0]
            temp_dice[3] = dice[5]
        # 서
        elif oper == 2:
            temp_dice[0] = dice[2]
            temp_dice[5] = dice[3]
            temp_dice[1] = dice[1]
            temp_dice[4] = dice[4]
            temp_dice[2] = dice[5]
            temp_dice[3] = dice[0]
        # 북
        elif oper == 3:
            temp_dice[0] = dice[4]
            temp_dice[5] = dice[1]
            temp_dice[1] = dice[0]
            temp_dice[4] = dice[5]
            temp_dice[2] = dice[2]
            temp_dice[3] = dice[3]
        # 남
        elif oper == 4:
            temp_dice[0] = dice[1]
            temp_dice[5] = dice[4]
            temp_dice[1] = dice[5]
            temp_dice[4] = dice[0]
            temp_dice[2] = dice[2]
            temp_dice[3] = dice[3]
        # 주사위 다시 세팅
        dice = temp_dice
        # 바닥면(dice[5]) 과 , 칸의 숫자 비교
        row = next_row
        col = next_col
        # 칸에 적힌 수가 0이아니면, 칸의수가 주사위에 복사 됨, 그리고 칸은 0이 됨
        if arr[row][col]:
            dice[5] = arr[row][col]
            arr[row][col] = 0
        # 0이면, 주사위 바닥면수가 칸에 복사
        else:
            arr[row][col] = dice[5]
        # 매번 윗면의 수를 출력
        result.append(dice[0])
    return result

N, M, X, Y, K = map(int, input().split())
MAP = [0] * N
for i in range(0 ,N):
    MAP[i] = list(map(int, input().split()))
O = list(map(int, input().split()))
ans = play_dice(MAP, N, M, O, X, Y)
for i in range(0, len(ans)):
    print(ans[i])