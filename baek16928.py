import sys
sys.stdin = open("baek16928.txt")

"""
DFS + 가지치기 // BFS 둘다 가능할듯?
일단 BFS로!

1과 100번에는 사다리/뱀이 없다!
사다리가 도착하는 칸은 중복될수 있답니다..
출발하는 칸은 하나가 맞음 

항상 중복을 조심하자!
BFS, DFS 같은경우 항상 
이게 가장 중요!!!
DP 를 쓰던, visited를 쓰던 필요없는 중복을 방지해야한다!
반례도 스스로 떠올릴수 있어야함!

DFS 에서 특정 값을 찾을때 바로 return하면 안되는 경우도 존재!
아래와같이 풀 수 있도록 주의할것

이 문제도, 어차피 같은 수를 또 방문했다면 이미 최소가 아니므로,
visited를 적용해야하는 문제!! + path 저장
"""

class Queue:

    def __init__(self, capacity): 

        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, x):

        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):

        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


def snake_ladder_game(snake, ladder):
    
    que = Queue(10000)
    # 현재위치, 주사위 횟수
    que.enqueue((1, 0))
    DP = [0] * (101)
    visited = [False] * 101
    
    while not que.is_empty():
        now = que.dequeue()
        num = now[0]
        path = now[1]
        for i in range(1, 7):
            next_num = num + i
            if next_num > 100:
                continue
            # 방문했던곳을 다시 방문하는것도 필요없음(최소를 구하므로)
            if visited[next_num]:
                continue
            if next_num in snake.keys():
                next_num = snake[next_num]
            elif next_num in ladder.keys():
                next_num = ladder[next_num]
            if visited[next_num]:
                continue
            visited[next_num] = True
            DP[next_num] = path+1
            que.enqueue((next_num, path+1))
    return DP[100]


N, M = map(int, input().split())
# key값이 있으면 value값으로 이동하는 형태로
L = {}
S = {}
for i in range(0, N):
    a, b = map(int, input().split())
    L[a] = b
for i in range(0, M):
    a, b = map(int, input().split())
    S[a] = b
ans = snake_ladder_game(S, L)
print(ans)