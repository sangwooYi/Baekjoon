import sys
sys.stdin = open("baek17178.txt")


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
    

N = int(input())
wait_list = [0] * N
sort_arr = [0] * (5*N)
idx = 0
for i in range(0, N):
    tmp = list(input().split())
    for j in range(0, len(tmp)):
        tmp[j] = tmp[j].split("-")
        tmp[j][1] = int(tmp[j][1])
        sort_arr[idx] = tmp[j]
        idx += 1
    wait_list[i] = tmp

sort_arr.sort(key=lambda x: (x[0], x[1]))

idx = 0
stk = Stack(5*N+100)

for i in range(0, N):
    for j in range(0, 5):
        now = wait_list[i][j]
        # 현재 사람이 가장 빠른경우
        if now == sort_arr[idx]:
            idx += 1
        else:
            # 스택안의 가장 나중에 들어온사람이 빠른순서일때
            while not stk.is_empty() and stk.peek() == sort_arr[idx]:
                stk.pop()
                idx += 1
            stk.push(now)

while not stk.is_empty() and stk.peek() == sort_arr[idx]:
    stk.pop()
    idx += 1

if stk.is_empty():
    print("GOOD")
else:
    print("BAD")
