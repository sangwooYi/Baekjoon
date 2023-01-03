import sys
sys.stdin = open("baek2357.txt")

"""
수의범위 1 ~ 1000000000

"""
def init_max_seg_tree(start, end, idx):
    if start == end:
        max_seg_tree[idx] = numbers[start]
        return max_seg_tree[idx]
    
    mid = (start+end)//2
    max_seg_tree[idx] = max(init_max_seg_tree(start, mid, 2*idx), init_max_seg_tree(mid+1, end, 2*idx+1))
    return max_seg_tree[idx]

def init_min_seg_tree(start, end, idx):
    if start == end:
        min_seg_tree[idx] = numbers[start]
        return min_seg_tree[idx]
    mid = (start+end)//2
    min_seg_tree[idx] = min(init_min_seg_tree(start, mid, 2*idx), init_min_seg_tree(mid+1, end, 2*idx+1))
    return min_seg_tree[idx]


def find_min_val(start, end, idx, left, right):
    
    if start > right or end < left:
        return INF
    if start >= left and end <= right:
        return min_seg_tree[idx]
    mid = (start+end)//2

    return min(find_min_val(start, mid, 2*idx, left, right), find_min_val(mid+1, end, 2*idx+1, left, right))

def find_max_val(start, end, idx, left, right):
    
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return max_seg_tree[idx]
    mid = (start+end)//2
    return max(find_max_val(start, mid, 2*idx, left, right), find_max_val(mid+1, end, 2*idx+1, left, right))

INF = 998876543211
N, M = map(int, sys.stdin.readline().split())
numbers = [0] * N
for i in range(0, N):
    numbers[i] = int(sys.stdin.readline())

max_seg_tree = [0] * (4*N)
min_seg_tree = [0] * (4*N)

init_max_seg_tree(0, N-1, 1)
init_min_seg_tree(0, N-1 ,1)


for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())

    min_val = find_min_val(0, N-1, 1, a-1, b-1)
    max_val = find_max_val(0, N-1, 1, a-1, b-1)
    print(f"{min_val} {max_val}")