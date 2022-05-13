import sys
sys.stdin = open("baek14891.txt")
"""
12시 1시 3시 5시 6시 7시 9시 11시 방향
[0,  0,  0,  0,  0,  0,  0,  0]
인덱스 기준 3시방향 == 2 , 9시방향 == 6
1: 시계  -1: 반시계 방향
맞닿는 부분은 각각 3시,  9시-3시,  9시-3시, 9시 이렇게이고,
극이 다르면 왼쪽 톱니와 반대방향 (*-1), 같은 극이면 같은방향으로 회전(*1)
회전 방향은, 동시에 움직이기떄문에, 현재 맞닿아있는 극
N극 0, S극은 1

따라서 각 회전때마다 회전시킨 톱니바퀴 번호, 방향이 주어짐
이때 각 바퀴마다 돌아가는 방향 지정한후, 회전 처리
=> 이걸 K번 반복하면 끝

K번 회전시킨 이후에, 각 12시방향 극이
1번 N극이면 0 S극이면 1
2번 N극이면 0 S극이면 2
3번 N극이면 0 S극이면 4
4번 N극이면 0 S극이면 8

오타 조심하자 ㅠㅠ
"""
# 시계 방향 회전
def rotate_clockwise(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

# 반시계방향 회전
def rotate_counter_clockwise(arr):
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp


def calc_point(gears, operations):
    # 각 기어마다 회전 방향을 체크, 1이면시계방향, -1이면 반시계, 0이면 회전 안함
    point = 0
    for i in range(0, len(operations)):
        # 매번 초기화
        rot_direct = [0] * 4
        # 돌릴 기어, 방향
        g, d = operations[i]
        g_idx = g-1
        # 회전 방향 (얘는 무조건 회전한다)
        rot_direct[g_idx] = d
        # 1번 기어
        if g_idx == 0:
            idx = 1
            # 3시 9시 여기부터 같은극이면 더 볼필요도 없다. 다를때만 진행
            while idx < 4:
                # 같은 극이면 더이상 회전 못함
                if gears[idx-1][2] == gears[idx][6]:
                    break
                # 다른극이면 반대방향 회전
                rot_direct[idx] = (rot_direct[idx-1] * -1)
                idx += 1
        # 2번 기어
        elif g_idx == 1:
            # 다른 극일 때만
            if gears[g_idx-1][2] != gears[g_idx][6]:
                rot_direct[g_idx-1] = (rot_direct[g_idx] * -1)
            idx = 2
            while idx < 4:
                # 같은 극이면 더이상 회전 못함
                if gears[idx-1][2] == gears[idx][6]:
                    break
                # 다른극이면 반대방향 회전
                rot_direct[idx] = (rot_direct[idx-1] * -1)
                idx += 1
        elif g_idx == 2:
            if gears[g_idx][2] != gears[g_idx+1][6]:
                rot_direct[g_idx+1] = (rot_direct[g_idx] * -1)                        
            idx = 1
            while idx >= 0:
                if gears[idx][2] == gears[idx+1][6]:
                    break
                rot_direct[idx] = (rot_direct[idx+1] * -1)
                idx -= 1
        elif g_idx == 3:
            idx = 2
            while idx >= 0:
                if gears[idx][2] == gears[idx+1][6]:
                    break
                rot_direct[idx] = (rot_direct[idx+1] * -1)
                idx -= 1
        # 회전 처리
        for j in range(0, 4):
            # 0이면 무시
            if rot_direct[j]:
                # 그냥 이렇게 넣어두면 내부가 알아서 바뀐다! 참조형이니까1
                if rot_direct[j] == 1:
                    rotate_clockwise(gears[j])
                elif rot_direct[j] == -1:
                    rotate_counter_clockwise(gears[j])
    for i in range(0, 4):
        # 있으면! (어차피 1또는 0이다) 1이 S극, 이때만 점수 얻을 수 있음
        if gears[i][0]:
            point += (2 ** i)
    return point


G = [[0] for _ in range(0, 4)]
for i in range(0, 4):
    G[i] = list(map(int, input()))
# 회전수
K = int(input())
O = [0] * K
for i in range(0, K):
    O[i] = list(map(int, input().split()))

answer = calc_point(G, O)
print(answer)