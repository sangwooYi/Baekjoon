import sys
sys.stdin = open("baek2457.txt")

"""
회의실 예약과 비슷 (스케줄링 문제)
반드시 다시 풀어보자.

겹치는 구간이 존재하는 한에서
가장 넓은 구간을 탐색하는 알고리즘을 짜야 하는 문제!

"""


N = int(sys.stdin.readline())
DAYS = [0] * N
for i in range(0, N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    # 이게 일단 첫번쨰 포인트
    DAYS[i] = (100*a+b, 100*c+d)
# 오름차순으로 일단 정리
DAYS.sort(key=lambda x : (x[0], x[1]))

# 선택한 갯수
count = 0
# 비교하는 기준으로 제일 늦게 지는 꽃
end = 0
# 3월 1일부터 시작, 마지막 꽃의 지는날을 의미
target = 301

while DAYS:
    # 종료조건 , 마지막 꽃이 지는 날이 12월 1일보다 이미 이상이거나, (진짜 끝)
    # 현재까지 남은 꽃 중 가장 빠른 피는 날이 target보다 큰 경우 (스케줄의 빈틈이 생김)
    if target >= 1201 or target < DAYS[0][0]:
        break

    for i in range(0, len(DAYS)):
        # 겹치는 구간이 존재하는 애들 중에서 가장 넓은 영역을 찾는 알고리즘
        if target >= DAYS[0][0]:
            # 현재 턴에서 가장 늦게 지는 꽃인 end보다 더 나중이면 갱신
            # 그래야 더 오래 볼 수 있다는 의미이므로
            if end <= DAYS[0][1]:
                end = DAYS[0][1]
            # 확인했으니 제거
            DAYS.remove(DAYS[0])
        # 겹치는구간 없으므로 이번 턴은 끝
        else:
            break
    # 이 1번의 반복이 한번의 선택인것
    # target 갱신
    target = end
    count += 1
if target < 1201:
    print(0)
else:
    print(count)