import sys
sys.stdin = open("baek15810.txt")

"""
mid 시간을 기준으로 할떄

M 이상 만들면 => right = mid
M 미만으로 만들면 left = right+1

"""


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 1
# 100만개를 1개당 100만개 걸리는사람이 혼자 만들때
right = 1000000000001

while left < right:

    mid = (left+right)//2

    cur_cnt = 0
    
    for i in range(0,  N):

        cur_cnt += mid//arr[i]
    
    if cur_cnt >= M:
        right = mid
    else:
        left = mid+1

print(left)