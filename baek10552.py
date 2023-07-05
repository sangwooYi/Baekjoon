import sys
sys.stdin = open("baek10552.txt")


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
        self.rear += 1
        self.data += 1

        if self.rear == self.max:
            self.rear = 0

        return x

    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.front += 1
        self.data -= 1

        if self.front == self.max:
            self.front = 0

        return now

    def is_empty(self):
        return self.data <= 0


def bfs(start):

    visited = [False] * (M+1)
    que = Queue(2*M)

    visited[start] = True
    que.enqueue((start, 0))

    while not que.is_empty():
        now, cnt = que.dequeue()

        # 현재 채널을 아무도 싫어하지 않으면 끝
        if len(hate_ch[now]) == 0:
            return cnt
        # 어차피 항상 첫번째 값이 가장 어린 사람
        man = hate_ch[now][0]

        next_ch = man_infos[man][0]

        if visited[next_ch]:
            continue
        visited[next_ch] = True
        que.enqueue((next_ch, cnt+1))

    return -1

N, M, P = map(int, sys.stdin.readline().split())

# 채널 1부터 M 까지
# 해당 채널을 싫어하는 사람 저장
hate_ch = [[] for _ in range(0, M+1)]

# 특정 사람이 좋아하는 채널, 싫어하는 채널 저장
man_infos = [0] * N
# 나이가 어린 순으로 주어지니까 굳이 정렬할 필요도 없음
for i in range(0, N):
    # a가 선호하는 채널 b가 싫어하는 채널
    a, b = map(int, sys.stdin.readline().split())
    
    man_infos[i] = [a, b]
    hate_ch[b].append(i)

ans = bfs(P)
print(ans)