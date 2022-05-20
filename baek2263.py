import sys
sys.stdin = open("baek2263.txt")
sys.setrecursionlimit(10**5)

"""
이문제 꼭 복습할것.
트리의 순회 연습!

기본적으로 중위순회를 이용하면 분할정복으로 노드 파악이 가능하다
좌 - 노드 - 우  이런식으로 분할정복이 가능함
그리고 후위순회는 마지막이 노드!
좌 - 우 - 노드
s
전위순회는 처음이 노드!
노드 - 좌 - 우

이 특성을 잘 활용할 수 있어야한다!

따라서 후위순회에서 마지막 부분을 찾아서 노드 체크
=> 이 노드값을 중위순회에서 찾아, 이걸 기준으로 좌/우 서브트리 분할
=> 이걸 분할정복

따라서 만약 전위 / 중위순회를 주고 => 후위순회를 출력해라
이런 문제도 동일한 로직으로 풀 수 있다!
"""


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# 전위순회에서 각 노드의 위치를 저장
node_pos = [0] * (N+1)
for i in range(0, N):
    # 현재 노드값의 위치 저장
    node_pos[in_order[i]] = i

answer = []
def pre_order(in_start, in_end, post_start, post_end):
    # 종료 조건!
    if (in_start > in_end) or (post_start > post_end):
        return
    # 부모노드 (후위순회로부터 찾는다.)
    parent = post_order[post_end] # 후위순회에서는 특정 서브트리 부분에서 마지막이 부모노드임
    
    # 노드 추가, 전위순회이므로, 최상위 부모 노드가 가장 먼저 나와줘야함.
    answer.append(parent)
    
    # 전위순회에서 해당 노드 위치를 기준으로, 좌 우를 나누는것
    left = node_pos[parent] - in_start # 왼쪽 서브트리 갯수  
    right = in_end - node_pos[parent] # 오른쪽 서브트리 갯수

    # 중위순회 / 후위순회를 각각 적절한 영역으로 쪼갠다.
    pre_order(in_start, in_start+left-1, post_start, post_start+left-1)
    # 중위순회는 부모노드가 in_start+left 위치이므로 이걸 pass, 후위순회는 가장끝에오므로 가장 끝을 pass
    pre_order(in_end-right+1, in_end, post_end-right, post_end-1)

pre_order(0, N-1, 0, N-1)
print(" ".join(map(str, answer)))