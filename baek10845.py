import sys
sys.stdin = open("baek10845.txt")


class Queue:
    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0
    
    def enqueue(self, x):
        if self.data >= self.max:
            return -1
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        # 배열의 인덱스가 self.max -1까지만 있기때문!
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):
        if self.data <= 0:
            return -1 
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now
        
    def is_empty(self):
        if self.data <= 0:
            return 1
        return 0

    def print_front(self):
        if self.data <= 0:
            return -1
        return self.que[self.front]
    
    def print_back(self):
        if self.data <= 0:
            return -1
        # 얘는 현재 self.rear위치 값은 비어있는 상태
        return self.que[self.rear-1]

    def size(self):
        return self.data


def baek10845(commands):
    q = Queue(len(commands)+10)
    for i in range(0, len(commands)):
        if commands[i][0] == "push":
            q.enqueue(int(commands[i][1]))
        elif commands[i][0] == "pop":
            print(q.dequeue())
        elif commands[i][0] == "size":
            print(q.size())
        elif commands[i][0] == "empty":
            print(q.is_empty())
        elif commands[i][0] == "front":
            print(q.print_front())
        elif commands[i][0] == "back":
            print(q.print_back())

N = int(input())
CDS = [0] * N
for i in range(0, N):
    CDS[i] = input().split()
baek10845(CDS)
