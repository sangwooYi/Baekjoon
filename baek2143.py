import sys
sys.stdin = open("baek2143.txt")

"""
맞든아니던
i 부터 j까지의 합을 계산하는 로직부터

ex) 
두 부분합이
각각 
2 / 3이 나온경우가 7가지 6가지이면 총 42가지가 있는것
이런식으로 따지면 100만 + 100만 + 100만 (마지막 key)이 최대 연산

point는 마지막에 100만 * 100만이아니라
A 의 dict key만 순회하면서
T - (a의 값) 이 B dict에 있는 경우만 계산하면 된다는게 point!
(그럼 O(N**4) => O(N**2)로 줄여주어서 시간 내에 풀이가 가능하도록 만들어 준다!)
"""


T = int(input())
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))


tmp_sum1 = [[0] * N for _ in range(0, N)]

tmp_sum2 = [[0] * M for _ in range(0, M)]
arr1_dict = {}
arr2_dict = {}
for i in range(0, N):
    temp = 0
    for j in range(i, N):
        temp += arr1[j]
        tmp_sum1[i][j] = temp
        if temp in arr1_dict.keys():
            arr1_dict[temp] += 1
        else:
            arr1_dict[temp] = 1
for i in range(0, M):
    temp = 0
    for j in range(i, M):
        temp += arr2[j]
        tmp_sum2[i][j] = temp
        if temp in arr2_dict.keys():
            arr2_dict[temp] += 1
        else:
            arr2_dict[temp] = 1

a = list(arr1_dict.keys())

answer = 0

for i in range(0, len(a)):
    # 어차피 합이 T가 되야하기때문에 이렇게만해도 가능!
    diff = T-(a[i])
    # 해당 값이 b dict에 있는경우만
    if diff in arr2_dict.keys():
        answer += (arr1_dict[a[i]] * arr2_dict[diff])
print(answer)