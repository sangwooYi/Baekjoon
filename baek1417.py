import sys
sys.stdin = open("baek1417.txt")
import heapq


N = int(input())

hq = []
scores = [0] * N

my_score = 0
for i in range(0, N):
    cur = int(input())
    if i == 0:
        my_score = cur
    else:
        # 최대힙으로 저장
        heapq.heappush(hq, -cur)

answer = 0
while hq:
    cur_score = heapq.heappop(hq)
    cur_score *= -1
    
    # 현재 저장된값중 가장 큰 값이 내 현재 점수 이상이면 -1빼서 다시 저장
    if cur_score >= my_score:
        answer += 1
        my_score += 1
        
        next_score = cur_score-1
        heapq.heappush(hq, -next_score)

print(answer)