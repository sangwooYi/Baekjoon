import sys
sys.stdin = open("baek10773.txt")

class Stack:
    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.data = 0
        self.ptr = 0
        
    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.ptr += 1
        self.data += 1
        return x
    
    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        self.data -= 1
        return self.stk[self.ptr]

    def is_empty(self):
        return self.data <= 0


K = int(sys.stdin.readline())
stk = Stack(K+10)
for i in range(0, K):
    now = int(sys.stdin.readline())
    if now == 0:
        stk.pop()
    else:
        stk.push(now)
answer = 0
while not stk.is_empty():
    temp = stk.pop()
    answer += temp
print(answer)