import sys
sys.stdin = open("baek16235.txt")

"""
시작은 전부 양분 5
아래 반복을 K 번한 뒤 살아남은 나무 구하는 문제

봄 : 양분 먹은 나무는 나이 +1 , 같은 칸에 여러 나무가 있다면, 어린 나무 부터  
    양분을 못먹은 나무는 바로 die (따라서 항상 나이순으로 정렬 해 줘야함.)

여름: 위에서 죽은 나무는 해당칸에 나이//2 만큼 양분을 추가 함 (위에서 temp이용, 죽은애는 제외하고 새로 만든다.)
가을 : 5k (5의배수) 나이를 가진 나무가 번식, 맵 안에 있는 범위내에서, 8방향으로 번식
       새로 생긴 나무의 나이는 무조건 1
    
겨울: S2D2가 A 배열에 담긴 양만큼 양분 추가 

조심할건 여기서 주어진 나무 위치의 r/c 값은  1부터 시작 난 0부터시작!   
"""


def after_k_years(arr, n, k, trees):
    
    # 초깃 값
    farm = [[5] * n for _ in range(0, n)]
    year = 0
        # 상 우상 우 우하 하 좌하 좌 좌상 
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    # arr[r][c].append([a, b]) 하려면 아래와같이 선언
    tree_info = [[[] for _ in range(0, n)] for _ in range(0, n)]
    
    # 초기 트리 저장
    for i in range(0, len(trees)):
        x, y, z = trees[i]
        # 해당 값에 나이만 저장해도 된다.
        tree_info[x-1][y-1].append(z)


    # k번 반복
    while year < k:
        # 봄, 여름
        for row in range(0, n):
            for col in range(0, n):
                now = tree_info[row][col]
                # 해당 값이 있는애만 체크하면 된다.
                if now:
                    # 살아남는 애
                    temp = []
                    # 죽을 애
                    die = []

                    # 여기서 정렬하는게 가장 효율적 (오름차순)
                    now.sort()
                    for t in range(0, len(now)):
                        # 아직 양분이 있으면 나이만큼 양분먹고 1살성장
                        age = now[t]
                        if farm[row][col] >= age:
                            farm[row][col] -= age
                            temp.append(age+1)
                        else:
                            # 양분이 부족하면 죽고, 본인 나이//2 만큼 양분으로 전환
                            conv = age//2
                            # 즉 전환될 양분이 1 이상인경우만 저장
                            if conv > 0:
                                die.append(conv)
                    # temp가 있으면 정렬후 저장
                    if temp:
                        temp.sort()
                    tree_info[row][col] = temp
                    # 양분 갱신
                    for j in range(0, len(die)):
                        # 해당 값만큼 양분 증가
                        farm[row][col] += die[j]
        # 가을, 나무 번식
        for row in range(0, n):
            for col in range(0, n):
                now = tree_info[row][col]
                # 역시 있는 경우만 인접한 칸에 나이가 5의 배수인 경우만 1짜리 나무를 추가 
                if now:
                    # 그냥 해당 횟수만큼 진행하면 됨
                    for t in range(0, len(now)):
                        if now[t] % 5 == 0:
                            for d in range(0, 8):
                                next_row = row + dr[d]
                                next_col = col + dc[d]
                                # 맵 밖일 경우
                                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                                    continue
                                # 나머지는 그냥 번식 1살짜리가 추가됨
                                tree_info[next_row][next_col].append(1)
        # 겨울, A 배열 값만큼 양분 증가
        for row in range(0, n):
            for col in range(0, n):
                farm[row][col] += arr[row][col]
        # 내년으로
        year += 1
    count = 0
    for row in range(0, n):
        for col in range(0, n):
            now = tree_info[row][col]
            if now:
                for i in range(0, len(now)):
                    count += 1
    return count
    

# N 땅크기, M 나무 수, K ~년후 살아남은 나무 구하기 (반복 수)
N, M, K = map(int, input().split())
# 매 겨울마다 해당 칸에 줄 양분의 값
A = [[0] * N for _ in range(0, N)]
for i in range(0, N):
    A[i] = list(map(int, input().split()))

TREE = [0] * M
for i in range(0, M):
    TREE[i] = list(map(int, input().split()))

answer = after_k_years(A, N, K, TREE)
print(answer)