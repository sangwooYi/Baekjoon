import sys
sys.stdin = open("baek16928.txt")

"""
DFS + 가지치기 // BFS 둘다 가능할듯?
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
    
    que = Queue(500000)
    # 현재위치, 주사위 횟수
    que.enqueue((1, 0))
    if 1 in ladder.keys():
        pos = ladder[1]
        if pos == 100:
            return 1
        que.enqueue((pos, 1))

    while not que.is_empty():
        now = que.dequeue()
        pos = now[0]
        time = now[1]

        for i in range(1, 7):
            next_pos = pos + i
            if next_pos > 100:
                continue
            if next_pos in snake.keys():
                next_pos = snake[next_pos]
                que.enqueue((next_pos, time+1))
            else:
                if next_pos in ladder.keys():
                    next_pos = ladder[next_pos]
                if next_pos == 100:
                    return time+1
                else:
                    que.enqueue((next_pos, time+1))



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