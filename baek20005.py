import sys
from collections import deque
sys.stdin = open("baek20005.txt")


"""
최대 26명의 1000*1000 맵
=> 일단 26명 각각 BFS 진행하여 플레이어별 필요 턴수를 구한뒤,
오름차순 
=> 현재 턴수에 해당하는 플레이어 수 만큼 ++ , 그 뒤 체력 남으면 다음턴으로 진행 
보스에 도달 못하는 경우는 없음!
"""

def bfs(player_pos, bos_pos):
    
    if player_pos == bos_pos:
        return 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False] * M for _ in range(0, N)]
    visited[player_pos[0]][player_pos[1]] = True

    que = deque()
    que.append((player_pos[0], player_pos[1], 0))

    while que:
        row, col, turn = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if MAP[next_row][next_col] == "B":
                return turn+1
            if MAP[next_row][next_col] == "X":
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, turn+1))
    


def calc_reward_count(boss_hp):

    # 플레이어별, 위치를 저장
    pos_of_players = [0] * P

    for row in range(0, N):
        for col in range(0, M):
            if MAP[row][col] == "." or MAP[row][col] == "X":
                continue
            if MAP[row][col] == "B":
                bos_pos = (row, col)
            else:
                player_name = MAP[row][col]
                idx_conv = player_idx[player_name] 
                pos_of_players[idx_conv] = (row, col)

    # key: 필요 턴수 value: [플레이어 수, 공격력 합]
    check_dict = {}
    for idx in range(0, P):
        start_row, start_col = pos_of_players[idx]
        
        req_turn = bfs((start_row, start_col), bos_pos)

        if req_turn in check_dict.keys():
            check_dict[req_turn][0] += 1
            check_dict[req_turn][1] += power_of_players[idx]
        else:
            check_dict[req_turn] = [1, power_of_players[idx]]
    
    req_turns = list(check_dict.keys())
    req_turns.sort()

    result = 0
    pre_turn = 0
    total_sum_power = 0
    for i in range(0, len(req_turns)):
        term = req_turns[i]-pre_turn-1
        # 해당 턴 이전턴 까지 들어가는 딜
        additional_deal = total_sum_power*term
        boss_hp -= additional_deal
        # 현재 턴 오기전에 보스가 죽어버린 경우 종료
        if boss_hp <= 0:
            return result

        player_cnt, sum_of_power = check_dict[req_turns[i]]
        pre_turn = req_turns[i]

        # 현재 턴에 추가된 인원만큼 합, 현재까지 누적딜만큼 hp 감소
        total_sum_power += sum_of_power
        result += player_cnt
        boss_hp -= total_sum_power

    return result

N, M, P = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(sys.stdin.readline().rstrip())

player_idx = {}
power_of_players = [0] * P
for i in range(0, P):
    name, power = sys.stdin.readline().split()
    player_idx[name] = i
    power_of_players[i] = int(power)
boss_hp = int(sys.stdin.readline())

answer = calc_reward_count(boss_hp)
print(answer)