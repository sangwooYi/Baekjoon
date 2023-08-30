import sys
sys.stdin = open("baek28278.txt")


class Stack:

    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.ptr = 0
        self.data = 0
    
    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.data += 1
        self.ptr += 1
        return x
    
    def dequeue(self):
        if self.data <= 0:
            return -1
        self.ptr -= 1
        self.data -= 1
        now = self.stk[self.ptr]
        return now
    
    def is_empty(self):
        if self.data <= 0:
            return 1
        return 0
    

    def peek(self):
        if self.data <= 0:
            return -1
        return self.stk[self.ptr-1]
    
    def data_cnt(self):
        return self.data
    

N = int(sys.stdin.readline().rstrip())
stk = Stack(2*N)

for i in range(0, N):
    tmp = list(map(int, sys.stdin.readline().split()))
    oper = tmp[0]

    if oper == 1:
        num = tmp[1]
        stk.enqueue(num)
    elif oper == 2:
        print(stk.dequeue())
    elif oper == 3:
        print(stk.data_cnt())
    elif oper == 4:
        print(stk.is_empty())
    else:
        print(stk.peek())