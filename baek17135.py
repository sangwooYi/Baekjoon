import sys
sys.stdin = open("baek17135.txt")

"""
거리는 (x1, y1) (x2, y2)일때
d = |x1-y2| + |y1-y2|  로 정의했음! (x축 좌표 차 + y축 좌표 차)
d <= D 일때만 죽일 수 있으며, 범위내에 여러적이 존재할 경우 가장 왼쪽 (가장 열이 작은 쪽) 부터!
범위내 적 사살 -> 남은 적들이 한칸씩 아래로 이동
성으로 도착시 그냥 게임에서 제외, 필드내에 적이 없어질 때까지 반복 하는것! 
가장 최대로 사살 가능한 적의 수를 찾는 문제
주의할 부분은 모든 궁수가 동시에 공격하므로
공격하는 순간에 공격 조건에 맞는 애만 공격한다는것!
(즉 안겹치게 쏘는게 아니라, 가장 가까우면서, 가장 왼쪽에 해당하는애를 겹치던 말던 쏘는것!)
=> 이부분 때문에 내가 틀린 것..

최대 행, 열이 15까지이고 궁수 배치의 극한 경우가 15C3 이므로 
(15*14*13//6 == 455) 극한의 경우가 455회 반복이라 가능! (브루트 포스)

"""

def calc_range(x1, y1, x2, y2):
    distance = abs(x1-x2) + abs(y1-y2)
    return distance


def find_max(arr, n, m, d):
    
    enemies = []
    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j]:
                # 적의 위치를 저장
                enemies.append([i, j])

    # MC3 (궁수를 배치할 수 있는 모든 경우)에 대해 반복한다.
    # nCr 에서 r 이정해진 경우는 for문으로 구현하는게 더 효율적 (재귀는 아무래도 더 오래걸림)
    archers = []
    for i in range(0, m):
        for j in range(i+1, m):
            for k in range(j+1, m):
                # 열 정보만 저장, 어차피 행은 N+1번째줄 고정이니까
                archers.append((i, j, k))
    result = 0
    # 배치 가능한 모든 궁수 위치에 대해 체크 
    for i in range(0, len(archers)):
        a, b, c = archers[i]
        # 궁수 배치
        archers_pos = [(n, a), (n, b), (n, c)]
        enemy = [0] * len(enemies)
        for j in range(0, len(enemies)):
            enemy[j] = enemies[j]
        # 적군 죽었는지 체크 용
        visited = [False] * len(enemies)
        visit_cnt = 0
        kill_point = 0
        while True:
            # 중복 제거
            tmp_kill = set()
            for j in range(0, 3):
                # 궁수 위치
                a_row, a_col = archers_pos[j]
                
                temp = []
                for k in range(0, len(enemies)):
                    # 아직 살아있는 애중에 사살 가능한 친구중 가장 가까운 적
                    # 그 친구들이 여러명이면 가장 열이 낮은 적을 먼저 사살해야함
                    if not visited[k]:
                        # 잡을수 있는애들을 전부 체크
                        distance = calc_range(a_row, a_col, enemy[k][0], enemy[k][1])
                        if distance <= d:
                            temp.append([distance, enemy[k][0], enemy[k][1], k])

            
                # 잡은애가 있을때만 진행, 가장가까운 적, 중복시 열이 가장 작은 적을 사살
                if temp:
                    temp.sort(key=lambda x : (x[0], x[2]))
                    tmp_kill.add(temp[0][3])
                # 다 잡았으므로 이게 최대 값이다. (종료조건을 여기에 두는거 괜찮을듯)
            tmp_arr = list(tmp_kill)
            if tmp_arr:
                for j in range(0, len(tmp_arr)):
                    visited[tmp_arr[j]] = True
                    kill_point += 1
                    visit_cnt += 1

            if kill_point == len(enemies):
                return kill_point
            if visit_cnt == len(enemies):
                break
                        
            # 아직 살아남은애들이 있다는 얘기 살아남은 적군들 한칸씩아래로
            for j in range(0, len(enemies)):
                if not visited[j]:
                    row, col = enemy[j]
                    next_row = row+1
                    if next_row >= n:
                        visited[j] = True
                        visit_cnt += 1
                        enemy[j] = [next_row, col]
                    else:
                        enemy[j] = [next_row, col]
            # 전부 필드에서 제외된 것
            if visit_cnt == len(enemies):
                break

        result = max(result, kill_point)
    return result


N, M, D = map(int, input().split())
# N+1 번쨰 (N 인덱스)가 필요하다! (궁수 위치)
MAP = [[0] * M for _ in range(0, N+1)]
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

answer = find_max(MAP, N, M, D)
print(answer)