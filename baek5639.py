import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek5639.txt")
"""
한줄 씩 읽는건 input() 혹인 sys.stdin.readline()

모든 줄을 다 읽어와야하는 문제는 sys.stdin.readlines()로 받아올것!

\n 이 개행 없애주는게 .rstrip() 인것!!
sys.stdin.readline() 쓸때도 만약 \n 딸려나오는 상황이면 .rstrip() 붙여주면 된다!

트리문제 기본!
만약 트리를 만들어야하는겨우에는 아래 2 step을 거친다.

완전 이진트리일떄
1. 노드 갯수 파악, 트리관계를 만듬 1번부터 N번 노드까지의 트리관계 (make_bin_tree)
2. 위에서 만든 트리를 중위순회를 돌려 노드값에 데이터를 저장 
(즉 노드의 데이터를 저장하고 싶으면 노드간 트리관계를 만든 후 ,중위순회를 돌리면 된다.)

tree = [[0] * 3 for _ in range(0, nodes+1)]
현재 노드기준 왼쪽자식노드 / 오른쪽자식노드 / 현재 노드의 값 이렇게 세개의 값을 갖는다
(포인터 개념이 들어간 것)
def make_bin_tree(nodes):
	# left노드, right노드, 현재노드의 데이터 이렇게 세가지 정보를 담는다!
    tree = [[0, 0, 0] for _ in range(0, nodes+1)]
    # node 가 n개가 있을때 마지막 부모가 될 수 있는 노드는 (n-1) //2 번! 
    for i in range(1, nodes//2+1):
        p = i
        left = 2 * i
        right = 2 * i + 1
        tree[p][0] = left
        if right > nodes:
            continue
        else:
            tree[p][1] = right
    return tree
 
def make_bin_search_tree(n):
    global data
    if n:
        make_bin_search_tree(bin_tree[n][0])
        data += 1
        bin_tree[n][2] = data
        make_bin_search_tree(bin_tree[n][1])

근데, 아래문제는 완전 이진트리는 아니다.

아래 문제 이해하고 자자..

전위순회는 노드부터 방문하므로
전위 = 노드 - 왼자 - 오자
중위 = 왼자 - 노드 - 오자
후위 = 왼자 - 오자 - 노드
첫번째로 주어진것은 루트 노드의 데이터값!
따라서, 현재 루트값보다 큰 순간부터는 오른쪽노드가 시작
ls 는 left + 1 부터,
re = right
rs = right + 1 부터로 우선 잡아놓는다. 
재귀 돌리면서 root보다 큰애가나오면 오른쪽노드의 시작값으로 설정
만약에 없어서 right+1  값이 그대로유지되면 그냥 그대로 진행되는것
le = rs - 1
루트 기준 바로 다음인덱스인
ls 부터 ~ le 까지는 노드기준 왼쪽 자식의 서브트리
rs 부터 re 까지는 노드기준 오른쪽자식의 서브트리
이걸 재귀를 돌려 분할정복을 하는것!
"""

def post_order(arr, left, right):
    global idx
    # 종료 조건 (따라서 right+1이 만약 최대노드 범위 벗어나거나 하면 여기서 끝나버림)
    if left > right:
        return
    # 현재 값
    node = arr[left]
    ls = left + 1
    re = right
    rs = right + 1
    for i in range(0, right-left+1):
        if i == 0:
            continue
        # 현재 노드값보다 큰애가 나오면 걔를 오른쪽 시작값으로
        if arr[left+i] > node:
            rs = i + left
            break
    # 왼쪽은 rs -1 에서 끝나야함
    le = rs - 1
    # 노드기준 왼쪽 서브트리
    post_order(arr, ls, le)
    # 노드기준 오른쪽 서브트리
    post_order(arr, rs, re)
    # 노드 방문
    answer[idx] = node
    idx += 1

t = sys.stdin.readlines()
pre_order = [0] * len(t)
for i in range(0, len(t)):
    if i == len(t)-1:
        pre_order[i] = int(t[i])
    else:
        pre_order[i] = int(t[i].rstrip())
idx = 0
answer = [0] * len(t)
post_order(pre_order, 0, len(t)-1)
for i in range(0, len(answer)):
    print(answer[i])