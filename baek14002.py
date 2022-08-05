import sys
sys.stdin = open("baek14002.txt")

"""
요 풀이는 N이 최대 1만까지만 가능한 풀이
O(N**2) 이므로, 이 이상은 NlogN으로 푸는 풀이로 해야함
=> NlogN풀이는 길이만 확정하며, 순서 출력시에는 별도에 알고리즘 추가 필요
"""

N = int(input())
arr = list(map(int, input().split()))


DP = [1] * N
ans_list = [0] * N
for i in range(0, N):
    ans_list[i] = str(arr[i])


for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            if DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
                ans_list[i] = ans_list[j] + " " + str(arr[i])

max_idx = 0
for i in range(1, N):
    if DP[max_idx] < DP[i]:
        max_idx = i
print(DP[max_idx])
print(ans_list[max_idx])