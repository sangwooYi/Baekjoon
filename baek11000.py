import sys
import heapq
sys.stdin = open("baek11000.txt")
"""
시작시간 기준으로 정렬하고,
우선순위는 종료시간으로 해야한다!
=> 가장 타이트하게 시간표를 짜려면
현재 기준, 가장 빨리 끝나는 애를 봐야한다.

이문제도 꼭 다시 풀어봐야함..
요새 너무 구글링을 자주하는거 아니냐 ㅡㅡ

그리고 너무 '그리디'에 함몰되지 말자. 결국 문제풀이를 해야하는것!
"""

N = int(sys.stdin.readline())
schedule = [0] * N
for i in range(0, N):
    s, t = map(int, sys.stdin.readline().split())
    schedule[i] = (s, t)
schedule.sort(key=lambda x : x[0])

hq = []
heapq.heappush(hq, schedule[0][1])
for i in range(1, N):
    # 비어있는 경우
    if not hq:
        heapq.heappush(hq, schedule[i][1])
    else:
        # 우선순위 큐는 자연스럽게 0번인덱스값이 가장 작은 값(최소 힙)
        if hq[0] <= schedule[i][0]:
            # 교체, hq 길이는 유지됨 이부분 때문에 내가 짰던 처음 코드가 틀린것, 다음 강의 종료시간으로 update하는 부분을 내가 안따졌었음.
            heapq.heappop(hq)
            heapq.heappush(hq, schedule[i][1])
        # 무조건 강의실이 필요한 경우 (길이가 늘어남)
        else:
            heapq.heappush(hq, schedule[i][1])
print(len(hq))
