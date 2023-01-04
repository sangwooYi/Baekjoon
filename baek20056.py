import sys
sys.stdin = open("baek20056.txt")

"""
입력
r, c : 행, 열
m : 질량
d : 방향  (0북 1북동 2동 3남동 4남 5남서 6서 7북서)
s : 속도

각자 d 방향으로 s 칸만큼 이동 후
겹쳐있는 파이어볼은 전부 합쳐지고
그 뒤 4개로 나뉨 (예시를 통해 체크 필요한 문제
1. 그냥 4개로 쪼개지고 원래위치에는 안남는다.  2. 무게는 소숫점은 버림으로 진행)
나뉠때 각 질량은 총합//5 , 속도는 총합//합쳐진수 질량 0 이하되면 그냥 소멸
합쳐지는 방향이 모두 홀or 짝이면 0246으로 // 아니면 1357로 쪼개짐 
=> 쪼개지기만하고 이동은 안한다!

주의할점은 1행과 N행이 // 1열과 N열이 연결된 상태라는것 (즉 경계선이 없다.....)
=> 즉 이동할때마다 속도//맵크기를 통해 실제로 이동하게 되는 칸 수를 반드시 체크해 주어야 함
+ 경계 넘어가는것 체크해주기

2차원 리스트 요소안에 빈리스트 사용?
"""
def conv_valid_point(point):
    if point < 0:
        point += N
    elif point >= N:
        point %= N
    return point


def set_next_stage_arr(arr):
    
    out_arr = []
    
    for row in range(0, N):
        for col in range(0, N):
            # 요소가 있을때만
            if len(arr[row][col]):
                f_m, f_s, f_d = arr[row][col][0]
                # 2개 이상일때는 계산해줄게 존재
                if len(arr[row][col]) > 1:
                    # 전부 홀수인지 전부 짝수인지 체크, 첫번째 요소기준으로 따져줘도 충분
                    f_check_flag = f_d%2 
                    flag = True

                    m_total = f_m
                    s_total = f_s
                    for k in range(1, len(arr[row][col])):
                        m, s, d = arr[row][col][k]
                        check_flag = d%2
                        # 한번이라도 다르면 boolean값 변경
                        if f_check_flag != check_flag:
                            flag = False
                        m_total += m
                        s_total += s
                    valid_m = m_total//5
                    # 소멸되었으면 끝
                    if valid_m <= 0:
                        continue
                    valid_s = s_total//len(arr[row][col])

                    # 0 2 4 6
                    if flag:
                        for dir in range(0, 8, 2):
                            out_arr.append((row, col, valid_m, valid_s, dir))
                    # 1 3 5 7
                    else:
                        for dir in range(1, 8, 2):
                            next_row = row + dr[dir]*valid_s
                            next_col = col + dc[dir]*valid_s

                            next_row = conv_valid_point(next_row)
                            next_col = conv_valid_point(next_col)
                            out_arr.append((row, col, valid_m, valid_s, dir))
                # 1개 뿐일때
                else:
                    out_arr.append((row, col, f_m, f_s, f_d))
    return out_arr


def find_total_after_operation(init_arr):

    stage = 1
    fire_ball_infos = init_arr
    while stage <= K:
        if len(fire_ball_infos) == 0:
            break
        tmp_map = [[[] for _ in range(0, N)] for _ in range(0, N)]
        
        for fire_ball in fire_ball_infos:
            # 행 열 질량 속도 방향
            r, c, m, s, d = fire_ball
            # 실제 이동하는 값
            valid_s = s%N
            
            next_r = r + dr[d]*valid_s
            next_c = c + dc[d]*valid_s
            next_r = conv_valid_point(next_r)
            next_c = conv_valid_point(next_c)

            tmp_map[next_r][next_c].append((m, s, d))
        
        fire_ball_infos = set_next_stage_arr(tmp_map)
        stage +=1
    answer = 0
    for i in range(0, len(fire_ball_infos)):
        answer += fire_ball_infos[i][2]
    return answer

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())

tmp_arr = [0] * M
for i in range(0, M):
    r, c, m, s, d = map(int, input().split())
    tmp_arr[i] = [r-1, c-1, m, s, d]

answer = find_total_after_operation(tmp_arr)
print(answer)