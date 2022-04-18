import sys
sys.stdin = open("baek16953.txt")


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


def find_num(a, b):
    que = Queue(1000000)
    INF = 9876543
    que.enqueue((a, 0))
    
    while not que.is_empty():
        now = que.dequeue()
        num = now[0]
        path = now[1]
        if num == b:
            return path+1
        for i in range(0, 2):
            if i == 0:
                double = num * 2
                if double > b:
                    continue
                que.enqueue((double, path+1))
            else:
                plus_one = int(str(num) + "1")
                if plus_one > b:
                    continue
                que.enqueue((plus_one, path+1))
    return -1

A, B = map(int, input().split())

ans = find_num(A, B)
print(ans)