import sys
import heapq
sys.stdin = open("baek12764.txt")

"""
일반적인 스케줄링 문제에서
시작시간 기준 정렬
heapq는 종료시간 기준 체크,
일반적으로는
힙큐 비어있으면 => 그냥 추가

===========================

if 현재 배정받은 방중 가장 빠른 종료시간 <= 현재 배정받을 시작시간 이면
  heapq 교체,
  else 추가 방이 필요한것
근데 여기선 "가장 작은 자리에 앉아야 한다' 라는 조건이 붙었으므로
"if 조건을 만족하는 조건의 모든 방을 체크 후, 가장 낮은 방번호와 교체"
해주어야 함, (N이 10만까지이므로, 속도가 나올지 체크)
=> 역시 시간초과..

** 조금만 사고를 확장시키자..
'비어있는 자리 중 가장 작은 번호'에 앉혀야 하므로,
차라리 시작시간 기준으로 heapq에 전부 담은 후 or 시간순으로 정렬한 후
순회하면서 0에서부터 배치하면서 배치되면 종료하는 방식을 사용한 것!
따라서 우선순위 큐를 심지어 안써도 된다! (문제의 특성을 잘 파악하자!)
"단순히 비어있는 강의실 체크 " vs "비어있는 자리 중 가장 작은 방부터 배정"

=> heapq를 쓰던, 정렬한 후 순회하던 시간은 거의 비슷하게 나온다!

"""


N = int(sys.stdin.readline())
# hq = []
times = [0] * N
for i in range(0, N):
    s, e = map(int, sys.stdin.readline().split())
    times[i] = (s, e)
    # heapq.heappush(hq, (s, e))

times.sort()
need = 0
# 배치 안되어있으면 그냥 0, 아니면 해당 자리에 종료시간을 배치함
computers = [0] * N 
count = [0] * N

for i in range(0, N):
    start, end = times[i]
    for i in range(0, N):
        if computers[i] <= start:
            if computers[i] == 0:
                need += 1
            computers[i] = end
            count[i] += 1
            break

# while hq:
#     start, end = heapq.heappop(hq)
#     for i in range(0, N):
#         # 현재 자리 종료시간 <= 현재 배정할 시작시간일 경우 배치 가능
#         if computers[i] <= start:
#             # 새로 배정받을 자리인것
#             if computers[i] == 0:
#                 need += 1
#             computers[i] = end
#             count[i] += 1
#             break
print(need)
answer = count[:need]
print(" ".join(map(str, answer)))
