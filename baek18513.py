import sys
sys.stdin = open("baek18513.txt")


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


def calc_min(arr, k):
    
    direct = [-1, 1]
    check = {}

    que = Queue(2000000)
    for i in range(0, len(arr)):
        que.enqueue((arr[i], 0))
        check[arr[i]] = 1
    
    res = 0
    cnt = 0
    while not que.is_empty():
        pos, distance = que.dequeue()

        for d in direct:
            next_pos = pos + d
            if next_pos in check.keys():
                continue
            check[next_pos] = 1
            next_dist = distance+1
            res += next_dist
            cnt += 1
            if cnt == k:
                return res
            que.enqueue((next_pos, next_dist))




N, K = map(int, sys.stdin.readline().split())
ponds = list(map(int, sys.stdin.readline().split()))

answer = calc_min(ponds, K)
print(answer)