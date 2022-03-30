"""
최소 / 최대힙 구현하는거 익혀두자
분할정복으로 가장 마지막 깊이의 부모에서부터 => (루트 - 마지막노드)
범위까지 확장시키면서 힙을 만드는 반복을 통해 구현한다!

1. upHeap, downHeap 구현 (left 제외 나머지 힙일 때 쓰는 메서드)
2. upHeap을 최소힙, downHeap을 반복하면 최대힙 구현 가능
   n개의 노드가 있을때 (n-1)//2 노드에서부터 시작해서 for((n-1)//2, -1, -1) 까지
   반복하면 된다!


이걸 계속 왔다리 갔다리 하려면 어떻게 ..?
계속 최소힙, 최대힙을 만드는 것을 반복해야하나 .?
힙만드는 복잡도는 O(logN) 따라서 100만이라도 20회정도 연산밖에 진행 안된다!

힙만들때 노드 규칙은 
i번쨰 노드 기준. 
부모노드는 (i - 1) // 2
왼쪽자식은 2*i + 1
오른쪽자식은 2*i + 2

따라서 힙만들떄 가장 마지막 노드가 right라면,
부모 노드는 (right - 1) // 2 까지만 탐색하면된다.
따라서
for range(0, (right-1) // 2 + 1) 로 되는것 


최소힙 최대힙 구현은 몇번 더 반복해보자
배열로 힙을 만들때는 반드시 루트 인덱스를 0으로 해야한다. 
"""
# 이 arr를 최대힙으로 만드는 것 (부모노드 < 자식노드
# 아래 downHeap , upHeap을 분할정복으로 돌려야 완성될듯
# left 제외하고 나머지가 힙인상태에서 가능한 로직
def downHeap(arr, left, right):
    temp = arr[left]
    parent = left

    # right 기준으로 부모는 (right - 1) // 2 이니까!
    while parent < ((right+1) // 2):
        # 왼쪽자식 cl 오른쪽자식 cr
        cl = parent * 2 + 1
        cr = cl + 1 
 
        if cr <= right and arr[cr] > arr[cl]:
            # 왼, 오 자식중에 큰값 갖는 노드값은 child로 대입
            child = cr
        else:
            child = cl
        # 이미 부모 노드값이 더 크면 중단 (가장 큰게 가장 머리노드에만 오면 되는거니까)
        if temp >= arr[child]:
            break
        # 큰값을 parent 노드에 대임
        arr[parent] = arr[child]
        # 자식 노드로 탐색 진행
        parent = child
    # 자식노드 자리에 temp 대입
    arr[parent] = temp


def upHeap(arr, left, right):
    temp = arr[left]
    parent = left
    
    # (right - 1) // 2 까지 탐색하는것, 부모노드가 가능한 마지막 노드임!
    while parent < (right + 1) // 2:
        cl = 2 * parent + 1
        cr = cl + 1
        if cr <= right and arr[cl] > arr[cr]:
            child = cr
        else:
            child = cl
        # 이미 최소힙인 경우
        if temp <= arr[child]:
            break
        # 작은값을 부모노드 자리에 넣고 
        arr[parent] = arr[child]
        parent = child
    # parent 칸에 temp를 대입해준다. (바뀌었건 안바뀌었건)
    arr[parent] = temp


# 아래처럼해야 전체를 최대힙 or 최소힙을 만드는것 
# 아래 노드부터 0번 노드까지 반복을 진행
# l ~ r 까지 완벽하게 최소 혹은 최대힙 만드는 메서드
def minHeap(arr, n):
    # n 노드 기준 가장 마지막부모노드는 (n-1) // 2
    start = (n-1) // 2
    for i in range(start, -1, -1):
        upHeap(arr, i, n-1)
    

def maxHeap(arr, n):
    start = (n-1) // 2
    for i in range(start, -1, -1):
        downHeap(arr, i, n-1)