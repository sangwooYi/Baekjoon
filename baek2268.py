import sys
sys.stdin = open("baek2268.txt")

"""
init 과정이 필요없다 처음엔 싹다 0!
"""

def update(start, end, idx, node_idx, value):
    
    # 애초에 세그먼트 트리는 a ~ b 부분까지의 특정 연산을 해둔것 따라서 탐색범위가 바꾼 요소 범위를 벗어나면 고려할 필요 X
    if node_idx < start or node_idx > end:
        return
    seg_tree[idx] += value
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, 2*idx, node_idx, value)
    update(mid+1, end, 2*idx+1, node_idx, value)


def calc_interval_val(start, end, idx, left, right):
    
    if end < left or start > right:
        return 0
    if end <= right and start >= left:
        return seg_tree[idx]
    mid = (start+end)//2
    return calc_interval_val(start, mid, 2*idx, left, right) + calc_interval_val(mid+1, end, 2*idx+1, left, right)


N, M = map(int, sys.stdin.readline().split())
MOD = 1
SUM = 0
seg_tree = [0] * (4*N)
arr = [0] * N 
for i in range(0, M):
    oper, a, b = map(int, sys.stdin.readline().split())

    if oper == SUM:
        left_pos = min(a, b)
        right_pos = max(a, b)

        interval_sum = calc_interval_val(0, N-1, 1, left_pos-1, right_pos-1)
        print(interval_sum)
    elif oper == MOD:
        pre_val = arr[a-1]
        arr[a-1] = b
        change_amount = b-pre_val
        update(0, N-1, 1, a-1, change_amount)
