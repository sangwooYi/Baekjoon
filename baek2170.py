import sys
sys.stdin = open("baek2170.txt")

"""
아이디어1
시작지점 기준 오름차순 정렬
=> 그 이후 
현재 종료지점 >= 다음 시작지점 이면
현재 시작지점 유지. 현재 종료지점은 max(현재 종료지점, 다음 종료지점)

만약 현재 종료지점 < 다음 시작지점이면
지금까지 거리 정산 + 현재 시작지점, 현재 종료지점 갱신
"""


N = int(sys.stdin.readline())
dots = [0] * N
for i in range(0, N):
    dots[i] = list(map(int, sys.stdin.readline().split()))

dots.sort()
answer = 0

start = dots[0][0]
end = dots[0][1]

if N == 1:
    answer = end-start

for i in range(1, N):
    now_s, now_e = dots[i]

    if end >= now_s:
        end = max(end, now_e)
        if i == N-1:
            answer += (end-start)        
    else:
        answer += (end-start)
        start = now_s
        end = now_e
        if i == N-1:
            answer += (end-start)
print(answer)