import sys
sys.stdin = open("baek7983.txt")


"""
초기 내 아이디어와 사실 거의 같다.

마감시간 기준 내림차순 이걸
그냥 선형으로 따지면서
매번 현재 마감기한과, now 를 따져서
마감기한 <=  now 이면 
마감기한 기준에서 work day만큼을 뺀값이 현재기준 now 가 되며,
마감기한 > now 이면
now 기준으로 work day를 뺀만큼이 현재기준 now 가 된다!

"""


N = int(sys.stdin.readline())
subjects = [0] * N
for i in range(0, N):
    d, t = map(int, sys.stdin.readline().split())
    # 최소 시작시간, 마감시간으로 저장
    subjects[i] = (d, t)

# 마감시한 기준으로 내림차순 
subjects.sort(key=lambda x : -x[1])

# 내가 쉴수있는 최대 기간이 된다.
now = subjects[0][1]-subjects[0][0]

for i in range(1, N):
    work_day, end_day = subjects[i]

    if end_day <= now:
        now = end_day-work_day
    else:
        now = now-work_day
print(now)