import sys
sys.stdin = open("baek17298.txt")

"""
이문제는, 이 문제를
스택으로 풀어야 한다는걸 깨닫는게 포인트!
어떤 문제에 스택/큐를 써야 하는지
혼자서 파악할 수 있어야 한다!
(이렇게 처음 초깃값보다 작 or 큰 값을 만날때 조치하는 문제들은 보통 스택!)
"""

class Stack:

    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.ptr = 0
        self.data = 0
    
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
        now = self.stk[self.ptr]
        return now
    
    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.stk[self.ptr-1]

    def is_empty(self):
        return self.data <= 0


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = [0] * N

stk = Stack(N+10)

for i in range(0, N):
    while not stk.is_empty() and stk.peek()[0] < nums[i]:
        num, idx = stk.pop()
        answer[idx] = nums[i]
    stk.push((nums[i], i))

while not stk.is_empty():
    num, idx = stk.pop()
    answer[idx] = -1
print(" ".join(map(str, answer)))