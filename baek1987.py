import sys
sys.stdin = open("baek1987.txt")

"""
문제를 잘 이해하자!
BFS / DFS 둘다 가능하며

DFS 로 풀려고 하는 경우, 
백트래킹 조건을 잘 잡아야 한다!

파이선에서 dict에서 key도 고유값을 갖는 hash지만

set도 마찬가지로, 순서가 없는 대신 고유한 값을 가진다!
따라서 a is 집합A => 이게 O(1) 임!

시간초과난 이유
=> dfs 좌표를 넘길때 tuple로 넘겨서, 
tuple => 좌표로 할당하는 시간이 문제였음
∴ dfs 쓸 때, 좌표는 tuple이나 list에 담아서 넘기지 말고,
인자로 바로 넘길 것!
+ 딕셔너리가 set보다 효율이 부족한 듯
"""


# 딕셔너리 대신, set로 푼 문제 
def dfs(row, col, path, check, arr):
    global answer

    answer = max(answer, path)

    for i in range(0, 4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        
        # 맵 밖이면 pass
        if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
            continue
        alph = arr[next_row][next_col]
        # 이미 지나간 알파벳이면 pass
        if alph in check:
            continue

        # 알파벳 경로 처리
        check.add(alph)
        dfs(next_row, next_col, path+1, check, arr)
        check.remove(alph)


R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

check = set()
check.add(MAP[0][0])
answer = 1
dfs(0, 0, 1, check, MAP)
print(answer)


# 내 풀이
# def dfs(row, col, path, check, arr):
#     global answer

#     answer = max(answer, path)

#     for i in range(0, 4):
#         next_row = row + dr[i]
#         next_col = col + dc[i]
        
#         # 맵 밖이면 pass
#         if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
#             continue
#         alph = arr[next_row][next_col]
#         # 이미 지나간 알파벳이면 pass
#         if check[alph]:
#             continue

#         # 알파벳 경로 처리
#         check[alph] = True
#         dfs(next_row, next_col, path+1, check, arr)
#         check[alph] = False


# R, C = map(int, input().split())
# MAP = [0] * R
# for i in range(0, R):
#     MAP[i] = list(input())

# # 상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# check = {}
# a = ord("A")
# for i in range(a, a+26):
#     check[chr(i)] = False
# check[MAP[0][0]] = True
# answer = 0
# # dfs 넘길때 그냥 좌표로 넘기자, 괜히 () 이렇게 튜플같은거로 넘기면 더 오래걸린다.
# dfs(0, 0, 1, check, MAP)
# print(answer)

