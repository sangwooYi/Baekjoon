from calendar import c
import sys
sys.stdin = open("baek18111.txt")

"""
최소시간 0 <= M, N <= 500 이므로 완전탐색 충분히 가능 
블록을 빼는데는 2초, 놓는데는 1초
인벤토리의 블록이 있는동안 놓는것만도 할 수 있다.

문제를 다른 시각으로 봐야하는 문제.
문제를 단순화 시키면, 오히려 이렇게 쉽게 풀릴 수도 있다!

(결국 내가 가용 가능한 블럭) // 한층을 만드는데 필요한 블럭 수
== 내가 쌓을 수 있는 최대 높이 요게 핵심인것!
단순화 시켜 구현 하는 연습 문제!

한번더 풀자!
"""

def mine_craft(arr, n, m, block):
    ans = []
    sum = 0
    for i in range(0, n):
        for j in range(0, m):
            sum += arr[i][j]
    avg = (sum + block) // (n * m)
    
    if avg >=256:
        max_height = 256
    else:
        max_height = avg
    
    for height in range(0, max_height+1):
        put = 0
        remove = 0
        for i in range(0, n):
            for j in range(0, m):
                # 빼야 함
                if height < arr[i][j]:
                    remove += (arr[i][j] - height)
                # 쌓아야 함
                elif height > arr[i][j]:
                    put += (height - arr[i][j])
        time = put * 1 + remove * 2
        ans.append((time, height))
    # 우선 시간순으로 내림차순 정렬, 그 안에선 높이순으로 오름차순 정렬
    ans.sort(key=lambda x: (-x[0], x[1]))
    return ans[-1]

# row: N   col: M
N, M, B = list(map(int, input().split()))
MAP = []
for i in range(0, N):
    now = list(map(int, input().split()))
    MAP.append(now)
answer = mine_craft(MAP, N, M, B)
print(answer[0], answer[1])