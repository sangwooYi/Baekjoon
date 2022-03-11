import sys
sys.stdin = open("baek2805.txt")

"""
괴랄한 숫자범위 받을떄
일단 이분탐색부터 떠올려보자..
이문제 무조건 다시 풀기
"""


def sum_of_len(arr, num):
    result = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] - num <= 0:
            break
        result += (arr[i] - num)
    return result

def find_max_height(trees,  n, m):
    pr = trees[n-1]
    pl = 0
    while pl <= pr:
        pc = (pl + pr) // 2
        now = sum_of_len(trees, pc)
        # 이분탐색 코드가 상황에따라 달라진다.
        # 이 문제는 now < m 인경우에만 확실히 줄이면되고
        # now >= m 인경우에는 일단 늘려보는것,
        # 그러다가 pl <= pr 범위 끝나면 그상태의 pr값을 반환하면 된다.
        if now >= m:
            pl = pc + 1
        else:
            pr = pc - 1
    return pr

N, M = map(int, input().split())
TREES = list(map(int, input().split()))
if N == 1:
    answer = TREES[0] - M
else:
    TREES.sort()
    answer = find_max_height(TREES, N, M)
print(answer)