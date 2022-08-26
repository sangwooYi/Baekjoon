import sys
sys.stdin = open("baek16397.txt")


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


def bfs(start, target, max_chance):
    if start == target:
        return 0
    visited = [False] * 100000
    que = Queue(100000)
    visited[start] = True
    que.enqueue((start, 0))

    limit = 99999
    while not que.is_empty():
        now, time = que.dequeue()

        for i in range(0, 2):
            if i == 0:
                next_num = now + 1
                if next_num > limit:
                    continue
            else:
                if now == 0:
                    continue
                next_tmp = now * 2
                if next_tmp > limit:
                    continue
                tmp = str(next_tmp)
                next_str = ""
                for j in range(0, len(tmp)):
                    if j == 0:
                        if tmp[j] != "1":
                            next_str += str(int(tmp[j])-1)
                    else:
                        next_str += tmp[j]
                next_num = int(next_str)
            if visited[next_num]:
                continue
            if next_num == target:
                return time+1
            
            if time+1 >= max_chance:
                continue
            visited[next_num] = True
            que.enqueue((next_num, time+1))
    return "ANG"

# N 현재수, T 클릭 가능 최대 횟수, G 목표 수
N, T, G = map(int, input().split())

answer = bfs(N, G, T)
print(answer)