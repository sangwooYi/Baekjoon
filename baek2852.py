import sys
sys.stdin = open("baek2852.txt")

"""

매번 input 받을떄마다 체크
스코어 반영 전에 
동점 상태인지, 한쪽이 이기고 있는지 체크

기본적으로 분단위로 체크한다

스코어 반영 후
동점 => 한쪽이 이기게 되면
last point 현재 시간으로 변경

한쪽이 이기는 상황 => 동점
이기고 있었던 팀 쪽에 현재시간-last point 만큼 시간 추가 

마지막 48분 기준으로 한쪽이 이기고있으면 현재시간 - last point 한번 더 진행

결과를 
시간 / 분으로 변환하여
HH : MM 으로 출력
"""


def get_win_team():
    
    res = -1
    if score[0] > score[1]:
        res = 0
    elif score[0] < score[1]:
        res = 1

    return res 


def conv_time_format(time_input):

    hour = time_input//60
    minute = time_input%60

    str_hour = str(hour)
    str_minute = str(minute)

    if hour < 10:
        str_hour = "0" + str_hour
    if minute < 10:
        str_minute = "0" + str_minute
    return str_hour + ":" + str_minute

score = [0, 0]
# 분단위로 저장후 변환하자
win_time = [0, 0]
# 동점이었던 마지막 시기 (분단위)
last_point = 0

N = int(input())
for i in range(0, N):
    team, time = input().split()
    # 인덱스로 변경
    t_idx = int(team)-1
    hour, minute = map(int, time.split(":"))
    # 분으로 변환
    total_min = 60*hour + minute

    win_team = get_win_team()
    score[t_idx] += 1

    # 동점이었다가 한쪽이 이기고 있게 된 상황
    if score[0] != score[1] and win_team == -1:
        last_point = total_min

    # 한쪽이 이기고 있다가 동점이 된 상황
    if score[0] == score[1] and win_team != -1:
        add_time = total_min - last_point
        win_time[win_team] += add_time

# 48분 마지막
fin_min = 60*48
# 한쪽이 이긴채로 끝났을 때만 추가 계산
if score[0] != score[1]:
    win_team = get_win_team()
    add_time = fin_min - last_point
    win_time[win_team] += add_time

for cur_time in win_time:

    ans = conv_time_format(cur_time)
    print(ans)