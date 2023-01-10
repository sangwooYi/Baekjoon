import sys
sys.stdin = open("baek14438.txt")

"""
세그먼트 트리
최댓값, 최솟값 업데이트까지 하는 방법!
"""

def init_seg_tree(start, end, idx):
    if start == end:
        seg_tree[idx] = numbers[start]
        return seg_tree[idx]
    mid = (start+end)//2
    seg_tree[idx] = min(init_seg_tree(start, mid, 2*idx), init_seg_tree(mid+1, end, 2*idx+1))
    return seg_tree[idx]

# 세그먼트 트리의 핵심은, 본인 범위가 아닐때는 무시하는 로직이 있어야한다는 것
# 여기서는 value는 진짜 바뀐 값을 넣어주어야 최솟값 판단이 가능해짐
def update_seg_tree(start, end, idx, arr_pos, value):
    
    if arr_pos < start or arr_pos > end:
        return seg_tree[idx]
    if start == end:
        # 이 탐색에서 start==end 까지 왔다면, arr_pos 인 것!
        seg_tree[idx] = value
        return seg_tree[idx]
    mid = (start+end)//2
    seg_tree[idx] = min(update_seg_tree(start, mid, 2*idx, arr_pos, value), update_seg_tree(mid+1, end, 2*idx+1, arr_pos, value))
    return seg_tree[idx]

def find_min_value(start, end, idx, left, right):
    if end < left or start > right:
        return 99999999999
    if end <= right and start >= left:
        return seg_tree[idx]
    mid = (start+end)//2
    return min(find_min_value(start, mid, 2*idx, left, right), find_min_value(mid+1, end, 2*idx+1, left, right))

N = int(sys.stdin.readline())
seg_tree = [0] * (4*N)
numbers = list(map(int, sys.stdin.readline().split()))

init_seg_tree(0, N-1, 1)

M = int(sys.stdin.readline())
for i in range(0, M):
    oper, a, b = map(int, sys.stdin.readline().split())

    if oper == 1:
        update_seg_tree(0, N-1, 1, a-1, b)
        numbers[a-1] = b
    else:
        find_seg_min = find_min_value(0, N-1, 1, a-1, b-1)
        print(find_seg_min)
