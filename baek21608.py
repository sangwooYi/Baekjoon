import sys
sys.stdin = open("baek21608.txt")

"""
아래 조건을 만족하게 
주어진 순서대로 학생을 배치하면 됨
배치 후, 각 학생마다 인접한 학생들 중, 좋아하는 학생이 들어간 인원수를 합산,
그 총합이 결과

1. 비어있는 칸중, 좋아하는 학생이 인접한 칸에 가장 많은칸으로
2. 1을 만족하는 칸이 여러개면, 인접한 칸중 비어있는 칸이 많은 칸으로
3. 2를 만족하는 칸도 여러개면 행의번호가 가장 작은 칸,
4. 3을 만족하는 칸도 여러개면 열의 번호가 가장 작은 칸
"""

def shark_school(students, size):
    
    n = size*size
    result = 0

    student_like = {}
    for idx in range(0, n):
        student_like[students[idx][0]] = students[idx][1:]

    like_score = [0, 1, 10, 100, 1000]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    pos_map = [[0] * size for _ in range(0, size)]

    for i in range(0, n):
        now = students[i][0]
        like = student_like[now]
        
        # 정렬을 위해 [인접한 칸에 좋아하는 학생 수, 인접한 칸에 비어있는 칸 수, 행, 열]
        # 위 요소로 남은 모든 칸을 탐색 후, 정렬하여 첫번째 요소 위치에 해당 학생을 배치!
        # 최대 학생수 400명
        tmp = []
        for r in range(0, size):
            for c in range(0, size):
                # 이미 배치되어있으면 pass
                if pos_map[r][c]:
                    continue

                like_cnt = 0
                empty_cnt = 0
                for d in range(0, 4):
                    next_row = r + dr[d]
                    next_col = c + dc[d]

                    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                        continue

                    pos = pos_map[next_row][next_col]
                    # 좋아하는 사람
                    if pos in like:
                        like_cnt += 1
                    # 비어있는 칸
                    if pos == 0:
                        empty_cnt += 1
                tmp.append((like_cnt, empty_cnt, r, c))
        tmp.sort(key=lambda x : (-x[0], -x[1], x[2], x[3]))
        check = tmp[0]
        pos_map[check[2]][check[3]] = now
    
    # 만족도 조사
    for r in range(0, size):
        for c in range(0, size):
            now = pos_map[r][c]
            like = student_like[now]

            cnt = 0
            for d in range(0, 4):
                next_row = r + dr[d]
                next_col = c + dc[d]
                
                if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                    continue
                if pos_map[next_row][next_col] in like:
                    cnt += 1
            result += like_score[cnt]
    
    return result       

N = int(input())
num = N*N
students = [0] * (num)
for i in range(0, num):
    students[i] = list(map(int, input().split()))

answer = shark_school(students, N)
print(answer)