import sys
sys.stdin = open("baek1463.txt")
"""
DP[숫자] = 연산 값 형태로 저장하고

만약 현재 해당 숫자까지 연산 값이
DP[숫자] <= 연산 횟수 이면 pass
DP[숫자] > 현재 연산 횟수인 경우에만
DP값을 갱신 ...
0.15초만에 이게 가능하려나
"""

# 이 DFS 방법은 가지치기 과정에서 필요한 과정이 잘리는 듯?
# 그렇다고 가지치기를 안하면 너무 재귀가 심하다..
# def dfs(now, path):
#     if now == 1:
#         if DP[1] > path:
#             DP[1] = path
#         return
#     n_path = path + 1
#     # 3으로 나누는 행위, 2로 나누는 행위, 1을 빼는 행위는 가능하다면 병렬적으로 진행되는것 따라서 각자 if
#     if (now % 3) == 0:
#         next = now // 3
#         # 이경우는 더이상 진행할 필요 X
#         if DP[next] < n_path:
#             return
#         DP[next] = n_path
#         dfs(next, n_path)
#     # 2로 나누어 떨어지면
#     if (now % 2) == 0:
#         next = now // 2
#         if DP[next] < n_path:
#             return
#         DP[next] = n_path
#         dfs(next, n_path)
#     # 항상 진행
#     next = now - 1
#     if DP[next] < n_path:
#         return
#     DP[next] = n_path
#     dfs(next, n_path)



# 메모이제이션, 위의 방법이 왜 안되는지는 고민해보자
# DP 는 아래처럼 쓰는것이 (메모이제이션) 기본!
# DP는 아래와 같이 쓰는것을 익히자.
N = int(input())

D = [0] * (N+1)
for i in range(2, N+1):
    D[i] = D[i-1] + 1
    if (i % 3) == 0:
        # 현재 값은 현재 저장된 값과, 이전 //3 값에서 한번 연산한 값중 최솟값 저장
        D[i] = min(D[i], D[i // 3]+1)
    if (i % 2) == 0:
        D[i] = min(D[i], D[i // 2]+1)
print(D[N])
