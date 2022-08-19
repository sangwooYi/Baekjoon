import sys
sys.stdin = open("baek3079.txt")

"""
풀이법 기억!

소요 시간을 mid = (left+right)//2 로 잡고.
해당 시간동안 각 입국소가 소화할 수 있는 수량을 합산함
(total += tasks[i] // mid) 
총 결과가 >= M 이상인 경우가 처음 나올떄까지 진행 (lower bound)
"""

N, M = map(int, sys.stdin.readline().split())

tasks = [0] * N
for i in range(0, N):
    tasks[i] = int(sys.stdin.readline())

# 가능한 최소 시간
left = min(tasks)
# 가능한 최대 시간 (이거와 아래 mid//tasks[i] 이 두가지가 핵심 포인트!)
right = max(tasks)*M
answer = right

while left <= right:
    mid = (left+right) // 2
    tmp = 0
    for i in range(0, N):
        # 해당 시간동안 처리할 수 있는 사람 수 (이 부분이 핵심이다!)
        tmp += (mid // tasks[i])

    # 목표 달성
    if tmp >= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
print(answer)