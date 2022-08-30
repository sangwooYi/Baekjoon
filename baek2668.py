import sys
sys.stdin = open("baek2668.txt")

"""
너무 어렵게 생각하지말자!

윗 줄 / 아랫 줄 따로 체크하며,

중복 방지위해 set 이용! 

3 1 1 2 이런 애들도 있으니까!
1부터 N 까지 순회하며 (dfs의 시작점)
각 dfs 마다 
=> now = nums[n]
not visited[now] 라면
up 에는 n  추가, down에는 now 추가
그 후 dfs(now)  재귀 진행
dfs 후 결과가 같다면 같은 애들끼리는 체크해서 정답에 append
다르다면 해당 값들은 false 처리
"""

def dfs(n):
    num = nums[n]
    if not visited[num]:
        visited[num] = True
        up.add(n)
        down.add(num)
        dfs(num)

N = int(input())
nums = [0] + [0] * N
for i in range(0, N):
    nums[i+1] = int(input())

visited = [False] * (N+1)
answer = []

for i in range(1, N+1):
    # set도 활용할 수 있으면 좋을듯
    up = set()
    down = set()
    dfs(i)
    if up == down:
        # set 도 for a in 세트 이방식으로 순회 가능함! (인덱스 접근은 불가!)
        for s in down:
            answer.append(s)
    else:
        for s in down:
            visited[s] = False
answer.sort()
print(len(answer))
for a in answer:
    print(a)