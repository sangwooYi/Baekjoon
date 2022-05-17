import sys
import heapq
sys.stdin = open("baek13904.txt")

"""
기본적으로 이런 형태의 문제는
우선순위 큐를 많이 가져간다!
why? 그리디 자체가 
"우선순위"를 이용하여 최대이익을 찾는 알고리즘이기 때문

1. 날짜는 오름차순, 같은 날짜중에서는 성적 내림차순으로 정렬
2. 현재 day >= data 그냥 push
# 이 부분이 핵심이다!!!!!!
3. else => heapq.pop해서 현재 data와 비교, 큰걸 push
"""

N = int(input())
arr = [0] * N
for i in range(0, N):
    arr[i] = list(map(int, input().split()))

arr.sort(key=lambda x: (x[0], -x[1]))
visited = [False] * N

hq = []
heapq.heappush(hq, (arr[0][1], arr[0][0]))
for i in range(1, len(arr)):
    day, score = arr[i]
    # 현재 오는 작업 처리 가능
    if len(hq) < day:
        heapq.heappush(hq, (score, day))
    # 안되면, 현재 hq중에서 최저점수를 pop해온다.
    # 어차피 push 기준, 작업처리 가능한 애들만 stack에 넣은것이므로!
    else:
        temp_score, temp_day = heapq.heappop(hq)
        if score > temp_score:
            heapq.heappush(hq, (score, day))
        else:
            heapq.heappush(hq, (temp_score, temp_day))

answer = 0
for i in range(0, len(hq)):
    answer += hq[i][0]
print(answer)