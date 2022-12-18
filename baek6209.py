import sys
sys.stdin = open("baek6209.txt")

"""
거의 다 풀었는데 ...

섬간 거리에 대한 arr를 계산한뒤 이를 순회
현재 돌의 누적거리가 
mid 미만이라면 그떄까지 섬 제거 cnt
mid 이상이 된 순간 누적 거리 reset

=> 최종 결과에서 cnt가 M개가 되는 값중 최댓값 찾기??
=> 

cnt >= M 이면 거리 늘리고  
cnt < M 이면 더 많이 쪼개야하므로 거리 줄이고  

upper bound 문제임
"""


D, N, M = map(int, input().split())
islands = [0] * N
for i in range(0, N):
    islands[i] = int(input())

islands.sort()

left = 0
right = D+1

while left < right:
    mid = (left+right)//2
    cnt = 0
    now = 0

    for island in islands:
        # 다음 거리까지 mid 보다 간격이 좁으면 그냥 섬 제거
        if island-now < mid:
            cnt += 1
        # mid 이상이면 다음 섬위치를 현재위치로 갱신
        else:
            now = island
            
    # 더 간격을 키워도 됨 (upper bound 진행)
    if cnt <= M:
        left = mid+1
    # 간격을 줄여야 함
    else:
        right = mid
print(left-1)