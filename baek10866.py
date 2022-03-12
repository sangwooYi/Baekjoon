import sys
sys.stdin = open("baek10866.txt")

class DeQue:
    
    def __init__(self, capacity):
        self.max = capacity
        self.deque = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0

    # 기본적으로 링 버퍼 사용
    # front는 현재 차있는상태,  rear은 비어있는상태 유지
    def push_front(self, x):
        if self.data >= self.max:
            raise IndexError
        self.front -= 1
        if self.front < 0:
            self.front == self.max - 1
        self.deque[self.front] = x
        self.data += 1
        return x

    def push_back(self, x):
        if self.data >= self.max:
            raise IndexError
        self.deque[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def pop_front(self):
        if self.data <= 0:
            return -1
        now = self.deque[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def pop_back(self):
        if self.data <= 0:
            return -1
        self.rear -= 1
        if self.rear < 0:
            self.rear = self.max - 1
        now = self.deque[self.rear]
        self.data -= 1
        return now

    def size(self):
        return self.data

    def empty(self):
        if self.data <= 0:
            return 1
        return 0

    def print_front(self):
        if self.data <= 0:
            return -1
        now = self.deque[self.front]
        return now
    
    def print_back(self):
        if self.data <= 0:
            return -1
        now = self.deque[self.rear-1]
        return now

def baek10866(commands):
    dq = DeQue(len(commands)+10)
    for i in range(0, len(commands)):
        command = commands[i]
        if command[0] == "push_front":
            temp = int(command[1])
            dq.push_front(temp)
        elif command[0] == "push_back":
            temp = int(command[1])
            dq.push_back(temp)
        elif command[0] == "pop_front":
            temp = dq.pop_front()
            print(temp)
        elif command[0] == "pop_back":
            temp = dq.pop_back()
            print(temp)
        elif command[0] == "size":
            print(dq.size())
        elif command[0] == "empty":
            print(dq.empty())
        elif command[0] == "front":
            print(dq.print_front())
        elif command[0] == "back":
            print(dq.print_back())

N = int(input())
CDS = [0] * N
for i in range(0, N):
    CDS[i] = input().split()
baek10866(CDS)