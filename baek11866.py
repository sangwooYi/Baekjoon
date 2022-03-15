import sys
sys.stdin = open("baek11866.txt")

"""
특정 루프를 돌떄 (a % 루프단위)
이 방법을 요긴하게 쓸 수 있다.
"""

def josephus(n, k):
    # 0 부터 n-1 까지
    visited = [False] * n
    # 인덱스와 실제값이 1차이
    idx = k-1
    # 실제 order에는 1 더해준값을 저장
    order = [idx+1]
    visited[idx] = True
    count = 1
    while count < n:
        time = 0
        while time < k:
            idx = (idx + 1) % n
            if visited[idx]:
                continue
            time += 1
        visited[idx] = True
        order.append(idx+1)
        count += 1
    return order

N, K = map(int, input().split())
answer = josephus(N, K)
print("<", end="")
for i in range(0, N):
    if i == N-1:
        print(answer[i], end="")
    else:
        print(answer[i], end=", ")
print(">")