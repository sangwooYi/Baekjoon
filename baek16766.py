import sys
sys.stdin = open("baek16766.txt")


"""
여기서 mid는 현재 탐색에서의
최대 대기시간 
따라서 우선 정렬 후,
다음 순회하는 소의 도착시간 - 처음 탑승 소 > mid 라면
다음 버스를 타는 것
그리고 만약 위 조건이 아니라도 정원 C가 되었으면 다음 버스 탑승

"""

N, M, C = map(int, sys.stdin.readline().split())
cows = list(map(int, sys.stdin.readline().split()))
cows.sort()

left = 0
right = 1000000000

while left < right:
    # 현재 탐색에서 최대 대기시간
    mid = (left+right)//2

    bus_cnt = 1
    board_cnt = 1
    time_first_cow_board = cows[0]
    total_max_waiting_time = 0
    for i in range(1, N):
        if board_cnt == C:
            bus_cnt += 1
            time_first_cow_board = cows[i]
            board_cnt = 1
        else:
            current_max_waiting = cows[i]-time_first_cow_board

            if current_max_waiting > mid:
                bus_cnt += 1
                time_first_cow_board = cows[i]
                board_cnt = 1
            else:
                board_cnt += 1

    # 너무 작은 범위를 설정함, 범위를 키워야 한다.
    if bus_cnt > M:
        left = mid+1
    else:
        right = mid
print(left)