import sys
sys.stdin = open("baek17143.txt")

"""
가장 오른쪽열의 오른쪽칸에 이동하면 멈춘다
그전까진 아래 단계가 반복
1. 오른쪽 1칸 이동
2. 낚시왕이 있는 열에 상어중 가장 가까운 상어 잡는다. (잡으면 사라짐) (열만 체크)
3. 상어가 이동

방향은 상 하 좌 우 순서임
상어 이동할때 벽에 부딪히면 남은 칸만큼 반대방향으로 움직인다,.
만약 이동을 마친후에 같은칸에 두마리 이상 있다면 크기가 가장 큰 상어만 살아남음

따라서 
col 기준 0부터 C-1 까지 순회하면 되며
매 순회마다 열을 0 부터 R-1까지 탐색해서 상어 찾아지면 바로 체크
상어 이동 처리, 이때 상어의 값을 매번 dict에 저장.
만약 겹치는 값이 나오면 더 큰값만 남긴다. (dict 갱신)
최종 dict 값을 사용해 다음 반복용 리스트를 생성하자. + 새로운 map 생성
"""

def calc_total(sharks, r, c):
    # 현재 낚싯꾼의 열 위치 0부터 c-1까지
    total = 0
    pos = 0

    # 상 하 우 좌
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    while pos < c:
        # 현재 낚시꾼 위치에서 가장 가까운 열에 상어 있으면 잡는다.
        box = [[0] * c for _ in range(0, r)]
        for i in range(0, len(sharks)):
            # 초기 입력 받을때 이미 가공해서 집어넣었다.
            row, col, s, d, z = sharks[i]
            box[row][col] = z
        
        
        flag = False
        catch_pos = [0, 0]
        for i in range(0, r):
            # 값이 있으면 잡는다.
            if box[i][pos]:
                flag = True
                catch_pos[0] = i
                catch_pos[1] = pos
                total += box[i][pos]
                break
        # 잡았을 떄만 sharks 재구성
        if flag:
            # 잡았으므로 하나 적은 길이가 된다.
            temp = [0] * (len(sharks)-1)
            idx = 0
            for i in range(0, len(sharks)):
                # 잡은 애가 있으면
                if sharks[i][0] == catch_pos[0] and sharks[i][1] == catch_pos[1]:
                    continue
                temp[idx] = sharks[i]
                idx += 1

            # sharks 재구성
            sharks = temp
        # 안잡았으면 그냥 이전 shark 그대로 쓴다.
        # 상어 이동
        # 위치 저장용
        temp_dict = {}
        for i in range(0, len(sharks)):
            row, col, s, d, z = sharks[i]
            # 우선 이동
            cnt = 0
            while cnt < s:
                cnt += 1
                next_row = row + dr[d]
                next_col = col + dc[d]

                # 맵 밖에 도달햇으면 방향 전환 (0 <-> 1 ,  2 <-> 3)
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    if d % 2:
                        d -= 1
                    else:
                        d += 1
                    row = row + dr[d]
                    col = col + dc[d]
                # 맵 안에 있으면 그냥 다음 반복 위한 갱신
                else:
                    row = next_row
                    col = next_col
            if (row, col) not in temp_dict.keys():
                # 속력, 방향 ,크기 저장해두어야함
                temp_dict[(row, col)] = [s, d, z]
            else:
                # 크기만 비교
                tmp = temp_dict[(row, col)][2]
                # 큰 경우만 갱신하면 됨
                if z > tmp:
                    temp_dict[(row, col)] = [s, d, z]
        tmp_d_keys = list(temp_dict.keys())
        temp = [0] * len(tmp_d_keys)
        idx = 0
        for i in range(0, len(tmp_d_keys)):
            row, col = tmp_d_keys[i]
            s, d, z = temp_dict[(row, col)]
            temp[idx] = [row, col, s, d, z]
            idx += 1
        sharks = temp
        pos += 1

    return total

# R행, C열, M상어의 수
R, C, M = map(int, input().split())

sharks = [0] * M
# (r, c)상어 처음 위치 s속력 d이동방향 z크기  (r c s d z) 로 주어짐
for i in range(0, M):
    r, c, s, d, z = map(int, input().split())
    # 상어 정보 저장, r, c 정보는 문제는 1부터 시작하니 1 감소시켜주고
    # 방항정보도 문제는 1부터시작하니 1 감소시켜야 함
    sharks[i] = [r-1, c-1, s, d-1, z]

answer = calc_total(sharks, R, C)
print(answer)