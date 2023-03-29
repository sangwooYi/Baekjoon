import sys
sys.stdin = open("baek18258.txt")


class Queue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.head = 0
        self.rear = 0

    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1

        if self.rear >= self.max:
            self.rear = 0
        return x
    
    def pop(self):
        if self.data <= 0:
            return -1
        now = self.que[self.head]
        self.data -= 1
        self.head += 1
        if self.head >= self.max:
            self.head = 0
        return now

    def size(self):
        if self.data <= 0:
            return 0
        return self.data
    
    def empty(self):
        if self.data <= 0:
            return 1
        return 0
    
    def front(self):
        if self.data <= 0:
            return -1
        return self.que[self.head]
    
    def back(self):
        if self.data <= 0:
            return -1
        return self.que[self.rear-1]
    

N = int(sys.stdin.readline())

que = Queue(N*2)
for i in range(0, N):
    tmp = list(sys.stdin.readline().split())

    operator = tmp[0]

    
    if operator == "push":
        num = int(tmp[1])
        que.push(num)
    else:
        answer = ""

        if operator == "pop":
            answer = que.pop()
        elif operator == "size":
            answer = que.size()
        elif operator == "front":
            answer = que.front()
        elif operator == "empty":
            answer = que.empty()
        elif operator == "back":
            answer = que.back()
        print(answer)