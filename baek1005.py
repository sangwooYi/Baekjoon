import sys
sys.stdin = open("baek1005.txt")
"""
아이디어1. (노드가 1000개라서 가능할지 사실 의문이긴 함. 최악의경우 깊이 1000까지 가야하므로 ㄷㄷ.) 
목표지점이 출발점이된다.
=> 이동 가능한 노드를 전부저장
=> 없으면 그냥 바로 본인 cost가 정답
=> 이동 가능한노드 존재시, 전부 탐색
=> 갈곳이 없을떄까지 탐색해야함
=> DFS를 통해 깊이탐색이 더 효율적일듯? 
=> 이미 방문한 지점이라면, 저장된값보다 클때만 업데이트 (문제 특성상 더 오래걸리는쪽이 그 노드까지 도달시간이 된다!)
=> 방문 가능한 최종노드들에 저장된 시간중에서 최솟값을 출력
"""

class Stack:
    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.data = 0
        self.ptr = 0

    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.data += 1
        self.ptr += 1
        return x
    
    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def isEmpty(self):
        return self.data <= 0


def acm_craft(graph, costs, w, n):
    stk = Stack(n*n)
    # cost는 0 ~  n-1까지, 실제 노드와 1차이씩난다 이부분 주의!
    stk.push((w, 0))



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    G = [[] for _ in range(0, N+1)]
    for i in range(0, K):
        a, b = map(int, sys.stdin.readline().split())
        G[a].append(b)
        G[b].append(a)
    W = int(input())
    