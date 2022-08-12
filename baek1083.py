import sys
sys.stdin = open("baek1083.txt")

"""
만약 횟수가 허락한다면
가장 큰수를 가장 앞으로 가져와야한다.

현재 위치보다 뒤에있는 수중에서 가장 큰 수와 비교해서 교환

"""

N = int(input())
nums = list(map(int, input().split()))
S = int(input())

for i in range(0, N-1):
    if S == 0:
        break
    mx, idx = nums[i], i
    
    #  현재 남은 교환 횟수 vs 최대 범위 중 작은값을 택한다.
    limit = min(N, i+1+S)
    # 선택 정렬과 유사하게, 현재 위치보다 뒤에 수중에서 가장 큰 수를 찾는것
    for j in range(i+1, limit):
        if mx < nums[j]:
            mx = nums[j]
            idx = j
    # 만약 현재 위치가 이미 최댓값이면 idx-i는 0이될것
    S -= (idx-i)
    # 해당 위치만큼 j-1위치의 값을 j위치에 대입해주고 mx 값은 i번 위치의 대입
    # idx == i라면 아래 반복문은 진행 안됨
    for j in range(idx, i, -1):
        nums[j] = nums[j-1]
    nums[i] = mx
print(" ".join(map(str, nums)))