import sys
sys.stdin = open("baek6198.txt")

"""
1. stk 비어있으면 바로 push
2. stk 있으면, 현재값과 스택의 peek 값을 비교
=> 현재값이 더 작으면 그냥 push 하고 다음으로 넘어감
=> 현재값이 peek 이상이면, 더 작은 값이 스택에 나올떄까지 계속 pop
마지막에 끝까지 남은 애들 체크해서 계산
"""


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
        self.data += 1
        self.ptr += 1
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




def calc_sum(arr):

    n = len(arr)
    stk = Stack(n*10)

    result = 0
    for idx in range(0, n):
        now = arr[idx]
        if stk.is_empty():
            # 값, 위치를 함께 저장
            stk.push([now, idx])
        else:
            # 바로 push
            if stk.peek()[0] > now:
                stk.push([now, idx])
            else:
                while not stk.is_empty() and stk.peek()[0] <= now:
                    h, pos = stk.pop()
                    result += (idx-pos-1)
                stk.push([now, idx])
    # 끝까지 남은애들 체크
    while not stk.is_empty():
        tmp, idx = stk.pop()
        result += (n-1-idx)
    return result



N = int(sys.stdin.readline())
H = [0] * N
for i in range(0, N):
    H[i] = int(sys.stdin.readline())

stk = Stack(N*10)
answer = calc_sum(H)
print(answer)