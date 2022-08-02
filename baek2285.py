import sys
sys.stdin = open("baek2285.txt")

"""
노드에 대해서만 체크하고,
전체 인구의 절반이 도달하는 지점을 찾아 반환

기본적으로 사람간의 거리의 합이므로
설치 위치 기준
좌  a명 / 우 b명 로 사람을 나누면
현재 기준에서 우측으로 1 이동할 때마다
좌측에서는 +a 우측에서는 -b만큼 거리의하 총합이 변한다.

따라서 전체 인구의 절반이 처음 초과되는 위치가 우리가 원하는 포인트!

why?

전체 인구 합이 total이고
i 번째 노드까지의 누적합이 S[i]라면
이렇게 누적합으로 푸는 문제들도 풀 수 있어야 한다!

i-1번째 노드 => i번쨰 노드로 이동 할때
거리합의 변화량 (Δ)는

+S[i] -(total-S[i]) 가 된다.

따라서 이 변화량이 가장 0에 가까워지는 지점은
처음 누적합이 전체 인원의 절반이 넘어가는 노드가 되는 것!
(해당 노드 전까지는 -변화량 그 다음 노드부터는 변화량이 +가 되므로!)
"""


N = int(sys.stdin.readline())
A = [0] * N
total = 0
for i in range(0, N):
    pos, num = list(map(int, sys.stdin.readline().split()))
    A[i] = [pos, num]
    total += num
# 위치 기준으로 오름차순
A.sort()

answer = 0
count = 0
for i in range(0, N):
    pos, num = A[i]
    count += num
    answer = pos
    # 누적합이 처음으로 전체 인구의 절반이 넘어가는 순간 break
    if count > total//2:
        break
print(answer)

