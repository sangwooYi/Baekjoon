import sys
sys.stdin = open("baek8980.txt")
"""
도착지점 순으로 정렬 (최대한 자주 내리고 실어야 한다.)
싣는 지점 => 내리는 지점
까지의 capa 배열 (수용 가능한 화물양)을 체크
그 사이에서의 최솟값 == 해당 구간에서 운송가능한 최대 운송치
이 값과, 현재 실을 수 있는 cost중에 최솟값을 사용
(음수가 되면 안되므로)

이거 너무 어렵다.. 풀이봐도 잘 모르겠네

무조건 다시 풀어볼 것..
"""

# 총 노드 , 최대 화물 갯수
N, C = map(int, input().split())
M = int(input())
MAP = [0] * M
for i in range(0, M):
    MAP[i] = list(map(int, input().split()))
MAP.sort(key=lambda x : x[1])
# 마을의 수용가능양 체크 // s ~ e-1까지만 보므로 얘를 N으로 해도 답이 맞았던것..
capa = [C] * (N+1)
answer = 0
for i in range(0, len(MAP)):
    s, e, cost = MAP[i]
    temp = C
    # s, 와 e 사이에서 capa[j]를 체크해서
    # 가장 작은 값이 실질적으로 운송 가능한 화물양
    for j in range(s, e):
        # 얘는 s - (e-1) 구간 사이에서 운송 가능한 최소 물량
        temp = min(temp, capa[j])
    # capa 배열이 음수가 되면 안되니까!
    # 즉 해당 구간에서 운송 가능한 최소 물량 vs 현재 포인트에서 실을 수 있는 물량
    # 이 값중에서 최솟값을 취해야 capa배열이 음수가 되지 않는다! 
    # + 과적재로 인해 다른 포인트에서 물건을 못 싣는 경우를 예방해 준다.
    temp = min(temp, cost)
    for j in range(s, e):
        capa[j] -= temp
    answer += temp
print(answer)