import sys
sys.stdin = open("baek12837.txt")


# 범위 안에 있을때만 체크하는것이 포인트
def update_tree(start, end, idx, node_idx, value):

    if node_idx < start or end < node_idx:
        return
    tree[idx] += value

    if start == end:
        return
    mid = (start+end)//2
    # 그냥 업데이트만 치면 됨
    update_tree(start, mid, 2*idx, node_idx, value) 
    update_tree(mid+1, end, 2*idx+1, node_idx, value)


def calc_interval_sum(start, end, idx, left, right):

    # 범위 밖이면 무시 (0을 반환해 주어야 재귀가 진행된다.)
    if end < left or start > right:
        return 0
    # 범위 안에 있으면 체크
    if left <= start and end <= right:
        return tree[idx]

    mid = (start+end)//2

    return calc_interval_sum(start, mid, 2*idx, left, right) + calc_interval_sum(mid+1, end, 2*idx+1, left, right)

N, Q = map(int, sys.stdin.readline().split())

# 초깃값은 0으로 시작
tree = [0]*(4*N)
arr = [0] * N
for i in range(0, Q):
    oper, p, q = map(int, sys.stdin.readline().split())

    if oper == 1:
        # 문제를 잘 읽자!
        update_tree(0, N-1, 1, p-1, q)
        arr[p-1] += q
    else:
        interval_sum = calc_interval_sum(0, N-1, 1, p-1, q-1)
        print(interval_sum)