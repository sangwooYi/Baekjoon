import sys
sys.stdin = open("baek10868.txt")

# 그냥 a ~ b 까지의 최솟값 저장
def init_tree(start, end, idx):

    if start == end:
        seg_tree[idx] = numbers[start]
        return seg_tree[idx]
    mid = (start+end)//2

    seg_tree[idx] = min(init_tree(start, mid, 2*idx), init_tree(mid+1, end, 2*idx+1))
    return seg_tree[idx]

# 범위에 올때만 체크
def find_min_val(start, end, idx, left, right):
    # 범위 벗어나면 무시
    if end < left or start > right:
        return INF
    
    if start >= left and end <= right:
        return seg_tree[idx]
    mid = (start+end) //2

    return min(find_min_val(start, mid, 2*idx, left, right) , find_min_val(mid+1, end, 2*idx+1, left, right))

N, M = map(int, sys.stdin.readline().split())

INF = 9987654321
seg_tree = [0] * (4*N)
numbers = [0] * N
for i in range(0, N):
    numbers[i] = int(sys.stdin.readline())

init_tree(0, N-1, 1)

for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    print(find_min_val(0, N-1, 1, a-1, b-1))