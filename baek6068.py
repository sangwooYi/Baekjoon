import sys
sys.stdin = open("baek6068.txt")


N = int(input())
schedules = [0] * N
for i in range(0, N):
    a, b = map(int, input().split())
    schedules[i] = (a, b)
schedules.sort(key=lambda x : -x[1])


answer = schedules[0][1] - schedules[0][0]
for i in range(1, N):
    # 답이 음수가 되면, 가능한 시간이 존재하지 않는것, 바로 종료
    if answer < 0:
        break
    req_time, limit_time = schedules[i]
    
    # 현재 가장 최고 효율의 시작시간과, 다음 탐색범위에서 마감시간을 비교
    # 마감시간이 더 이전이면, answer 값은 마감시간에서 req_time만큼 차감
    if limit_time < answer:
        answer = limit_time-req_time
    # limit_time >= answer 라면, 결국 그냥 현재 answer 값에서 req_time만큼을 차감
    else:
        answer = answer-req_time
if answer < 0:
    answer = -1
print(answer)
