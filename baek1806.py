import sys
sys.stdin = open("baek1806.txt")

"""
투포인터 알고리즘??
start, end 둘다 0에서 시작
구간합 < N 이면 start + 1
구간합 >= N이면 end + 1
(만약 N 이면 길이 체크, 최소길이만 갱신)
"""


N, M  = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

INF = 987654321
answer = INF

start = 0
end = 0
tmp_sum = arr[0]

while end < N and start <= end:
    # 구간합이 아직 M 미만, end를 증가
    if tmp_sum < M:
        n_end = end + 1
        # 범위 끝
        if n_end >= N:
            break
        # 가능하면 다음 요소를 포함
        end = n_end
        tmp_sum += arr[n_end]
    # 구간합 M 이상인 경우
    else:
        # 현재 길이 체크해서 최단길이 갱신
        answer = min(answer, end-start+1)
        # start < end 상황이면 start 포인트를 하나 앞으로, 직전 요소 제외 
        if start < end:
            tmp_sum -= arr[start]
            start += 1
        # start == end 였다면 최단길이 1인 상황이므로 더 볼필요 없다. 
        else:
            break


# 한번도 체크 안된경우
if answer == INF:
    answer = 0

print(answer)