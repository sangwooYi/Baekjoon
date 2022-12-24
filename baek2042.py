import sys
sys.stdin = open("baek2042.txt")


"""
세그먼트 트리 연습문제
"""

# 세그먼트트리 초기 세팅
# start: 배열의 시작점  end: 배열의 끝점  idx: 세그먼트 트리의 인덱스 (1부터 시작 
# why? 그래야 2*idx 가 왼쪽 자식, 2*idx+1 이 오른쪽 자식이 되는 분할정복이 가능하므로!)
def init_seg_tree(start, end, idx):
    
    if start == end:
        tree[idx] = numbers[start]
        return tree[idx]

    mid = (start+end) // 2

    # 왼쪽 자식 / 오른쪽자식 분할정복 모든 이진트리 노드에대해 본인이 갖고있는 왼쪽자식 / 오른쪽자식 값의 합을 취함
    tree[idx] = init_seg_tree(start, mid, idx*2) + init_seg_tree(mid+1, end, idx*2+1)
    return tree[idx]

# 구간 합 구하는 메서드
# start~end: 현재 탐색중인 구간 idx: 세그먼트 트리 인덱스, left/right 구간합을 구하고자 한는 범위
# 범위 안에 있을 때 해당 값을 가져오는게 point
def calc_interval_sum(start, end, idx, left, right):
    # 구간 합 범위 밖
    if left > end or right < start:
        return 0
    # 구간합 목표 범위 안
    if left <= start and right >= end:
        return tree[idx]

    # 아니면 분할하여 정복 (right >= start and left <= end 이면서 right > end or left > start 인 경우)
    mid = (start+end) // 2
    return calc_interval_sum(start, mid, idx*2, left, right) + calc_interval_sum(mid+1, end, idx*2+1, left, right)

# numbers 배열에서 특정 노드값이 변할때 세그먼트트리 업데이트 해주는 메서드 
# 세그먼트트리 == 구간합이므로, 해당 노드를 범위로 갖는 모든 세그먼트트리의 모든 노드가 업데이트 되어야 함 
# start~end: 탐색하는 구간 idx: 세그먼트 트리 인덱스 what: 구간합 수정하려는 노드 인덱스 value: 수정하려는 수치
def update(start, end, idx, what, value):

    # 범위 밖
    if what < start or what > end:
        return
    
    tree[idx] += value
    # 가장 마지막 자식 트리
    if start == end:
        return
    mid = (start+end) // 2
    # 하위 자식트리들 전부 업데이트 해주어야 함
    update(start, mid, idx*2, what, value)
    update(mid+1, end, idx*2+1, what, value)

N, M, K = map(int, sys.stdin.readline().split())
numbers = [0] * N
# 배열 길이 N 에 가장 가까운 제곱수 * 2 만큼의 길이가 필요 (그래서 그냥 4배 때린다)
tree = [0] * (N*4)
NODE_CHANGE = 1
PRINT_NODE = 2

for i in range(0, N):
    numbers[i] = int(sys.stdin.readline())

# 초기 세그먼트 트리 (세그먼트트리 인덱스는 1부터 시작하게 세팅한다 무조건!)
init_seg_tree(0, N-1, 1)

for i in range(0, (M+K)):
    oper, b, c = map(int ,sys.stdin.readline().split())

    if oper == NODE_CHANGE:
        # b번쨰 원소를 c로 교체
        pre_num = numbers[b-1]
        # 업데이트 되어야할 수치 (양수가 될수도 있고 음수가 될수도 있고)
        change_quantity = c-pre_num
        # 요소 값을 실제로 바꿔주어야 함
        numbers[b-1] = c
        update(0, N-1, 1, b-1, change_quantity)

    elif oper == PRINT_NODE:
        interval_sum = calc_interval_sum(0, N-1, 1, b-1, c-1)
        print(interval_sum)