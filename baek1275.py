import sys
sys.stdin = open("baek1275.txt")


# 세그먼트 트리 초기화
def init_seg_tree(start, end, idx):

    if start == end:
        seg_tree[idx] = elements[start]
        return seg_tree[idx]
    
    mid = (start+end)//2
    seg_tree[idx] = init_seg_tree(start, mid, 2*idx) + init_seg_tree(mid+1, end, 2*idx+1)
    return seg_tree[idx]

# 요소 값 업데이트 // 해당 요소의 값을 바꿀때 세그먼트트리 업데이트 ./// 탐색 범위 안에 요소 위치가 있을때만 계산
def update(start, end, idx, element_idx, value):
    
    # 범위 밖
    if element_idx < start or element_idx > end:
        return
    seg_tree[idx] += value
    
    # 가장 마지막 트리
    if start == end:
        return
    mid = (start+end)//2
    
    update(start, mid, 2*idx, element_idx, value)
    update(mid+1, end, 2*idx+1, element_idx, value)


# 구간합 구하기, 탐색 범위가 구하려는 구간 안에 들어올 때만 고려
# start~end 탐색 범위 // left~right 구하려는 구간합
def calc_interval_sum(start, end, idx, left, right):

    # 구간 밖
    if start > right or end < left:
        return 0
    
    # 탐색 범위가 구하려는 구간 안에 들어온 경우  left  start   end  right  이런 경우임!
    if start >= left and end <= right:
        return seg_tree[idx]

    mid = (start+end)//2

    # 자식 노드의 각 값의 합이 현재 노드의 값이 된다.
    return calc_interval_sum(start, mid, 2*idx, left, right) + calc_interval_sum(mid+1, end, 2*idx+1, left, right)


N, Q = map(int, sys.stdin.readline().split())
seg_tree = [0] * (4*N)
elements = list(map(int, sys.stdin.readline().split()))

init_seg_tree(0, N-1, 1)

for i in range(0, Q):
    # x~y 까지의 합을 구한 후 // a번째 수를 b로 바꿔야 함
    # x <= y 가 보장되어있지 않다.. 조심
    x, y, a, b = map(int, sys.stdin.readline().split())
    
    min_num = min(x, y)
    max_num = max(x, y)

    interval_sum = calc_interval_sum(0, N-1, 1, min_num-1, max_num-1)
    print(interval_sum)

    pre_element = elements[a-1]

    change_quantity = b-pre_element
    elements[a-1] = b
    update(0, N-1, 1, a-1, change_quantity)
    
