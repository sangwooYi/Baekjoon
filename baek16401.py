import sys
sys.stdin = open("baek16401.txt")

"""
현재 탐색값이 a 일때
a 보다 짧은길이 과자는 pass
a 보다 긴 길이의 과자일 때는 => 남은 길이 >= a 인지 체크

결과가 N개 이상이나오면 => 탐색길이를 늘린다.
N개 미만이 일대는 탐색길이를 줄인다.
"""

M, N = map(int, sys.stdin.readline().split())
crackers = list(map(int, sys.stdin.readline().split()))

left = 1
# 최대 과자길이 10억
right = 1000000001

while left < right:
    mid = (left+right)//2
    
    cnt = 0
    for cracker in crackers:
        cur_len = cracker

        while cur_len >= mid:
            cnt += 1
            cur_len -= mid
    if cnt >= M:
        left = mid+1
    else:
        right = mid
print(left-1)