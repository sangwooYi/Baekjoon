import sys
sys.stdin = open("baek5676.txt")

"""
세그먼트트리 곱하기버전!

이 문제는 부호만 알면되므로 정확한 값이아닌
부호판단을위한 값으로 대체할 수 있음! (특수한 문제)
따라서 애초에 요소값이 > 0 이면 1   < 0 이면 -1 0이면 0으로 요소값을 대체하고

update도 그냥 1 / -1 / 0 을 해당 세그트리값에 대입하는 형식으로 푼다!

세그먼트 트리의 개념을 이해하자!
"""


def pmz(num):# 양수,음수,0 반환하는 함수
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else: 
        return 0

def init_seg_tree(start, end, idx):

    if start == end:
        # 부호 여부만 알면되므로 1/-1/0으로 환산 (idea!)
        arr[start] = pmz(arr[start])
        seg_tree[idx] = arr[start]
        return seg_tree[idx]

    mid = (start+end)//2
    seg_tree[idx] = init_seg_tree(start, mid, 2*idx) * init_seg_tree(mid+1, end, 2*idx+1)
    return seg_tree[idx]


def calc_interval_multiple(start, end, idx, left, right):
    # 항등원을 반환해야함
    if end < left or start > right:
        return 1
    
    if left <= start and right >= end:
        return seg_tree[idx]

    mid = (start+end)//2
    return calc_interval_multiple(start, mid, 2*idx, left, right)*calc_interval_multiple(mid+1, end, 2*idx+1, left, right)

def update(start, end, idx, pos, value):

    if pos < start or pos > end:
        return
    
    if start == end:
        seg_tree[idx] = value
        return

    mid = (start+end)//2 
    update(start, mid, 2*idx, pos, value)
    update(mid+1, end, 2*idx+1, pos, value)
    # 세그먼트 트리의 핵심! 해당 트리노드는 왼쪽 / 오른쪽 자식의  합 or 곱 or 특정 연산값인것!
    seg_tree[idx] = seg_tree[2*idx] * seg_tree[2*idx+1]


while True:
    tmp = sys.stdin.readline().split()
    # TC 가 정해져있지않을때 종료조건
    if len(tmp) == 0:
        break
    N, K = map(int, tmp)
    seg_tree = [0] * (4*N)

    arr = list(map(int, sys.stdin.readline().split()))
    init_seg_tree(0, N-1, 1)

    answer = ''
    for i in range(0, K):
        oper, a, b = sys.stdin.readline().split()
        a = int(a)  
        b = int(b)
        # a번재위치값을 (인덱스는 a-1) b로 교체
        if oper == "C":
            arr[a-1] = pmz(b)
            update(0, N-1, 1, a-1, pmz(b))
    
        else:
            interval_mult = calc_interval_multiple(0, N-1, 1, a-1, b-1)
            if interval_mult > 0:
                answer += "+"
            elif interval_mult < 0:
                answer += "-"
            else:
                answer += "0"
    print(answer)