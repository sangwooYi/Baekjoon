import sys
sys.stdin = open("baek2343.txt")


"""
항상 left / right 를 잘 정해야한다!
left = max(lectures)
right = 10000*10만
mid가 녹화시간
누적값이 녹화시간이 넘어가면 넘어감
=> 이 덩어리가 M 개여야 함.
가능한 최솟값을 찾아야 하므로,
M개보다 같거나 작으면 탐색범위를 줄이고,
M개보다 크면 탐색범위를 늘린다.
"""

N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))


left = max(lectures)
right = 1000000001

answer = right
while left < right:
    mid = (left+right)//2

    cnt = 1
    tmp_sum = lectures[0]
    for i in range(1, N):
        tmp_sum += lectures[i]

        if tmp_sum > mid:
            cnt += 1
            tmp_sum = lectures[i]

    if cnt > M:
        left = mid+1
    else:
        right = mid
print(left)