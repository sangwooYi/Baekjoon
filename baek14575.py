import sys
sys.stdin = open("baek14575.txt")

"""
현재 탐색 기준 A일때

A 가 한사람이라도 Li 보다 작거나 Ri보다 크면 바로 종료.
Li보다 작은경우면 => 값을 키우고
Ri보다 큰경우면 => 값을 줄인다.

만약 위 조건이 다된다면
min(Ri, A) 값의 총합을 구함
모든사람이 A 이하로만 받으면 문제가 없는 것 

이 sum이 T 이상이면 => 다음값 줄이고
T보다 작으면 다음값 늘린다.

lower bound

항상 불가능하다면 -1 출력
"""

N, T = map(int, input().split())

arr = [0] * N

max_sum = 0
min_sum = 0
for i in range(0, N):
    l, r = map(int, input().split())
    arr[i] = [l, r]

    max_sum += r
    min_sum += l
# 최대치로 받아도 T가 안되거나, 최소치로 받아도 T가 넘어갈때는 불가능
if max_sum < T or min_sum > T:
    print(-1)
else:
    left = 1
    right = 1000000001

    while left < right:

        mid = (left+right)//2

        total = 0
        flag = True
        # 한사람이라도 l 보다 낮으면 안됨
        for i in range(0, N):
            
            l, r = arr[i]

            if mid < l:
                flag = False
                break
            total += min(r, mid)

        if not flag:
            left = mid+1
        else:
            if total >= T:
                right = mid    
            else:
                left = mid+1

    print(left)
