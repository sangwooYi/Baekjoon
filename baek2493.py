import sys
sys.stdin = open("baek2493.txt")


"""
우측부터 왼쪽으로 진행,

스택이 비어있으면 무조건 push
스택이 있다면
현재 가장 top에 있는 값(peek)과 비교,

현재 타워 < peek 값 이면
그냥 push

현재 타워 >= peek 이라면
현재 타워 < peek 값이 나올때까지 pop하고 위치 기록

스택에 남아있는 애들은 그냥 여기선 따로 계산할 필요 X
(굳이 한다면 전부 0으로 처리해주면 됨, 근데 디폴트값이 0이니까 불필요)
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
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.stk[self.ptr-1]

    def is_empty(self):
        return self.data <= 0


N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

stk = Stack(N+100)
res = [0] * N

for i in range(N-1, -1, -1):
    now = towers[i]

    # 스택 비어있으면 무조건 push
    if stk.is_empty():
        stk.push([now, i])
    else:
        while not stk.is_empty() and now >= stk.peek()[0]:
            h, idx = stk.pop()
            res[idx] = i+1   # 위치 값은 1부터 시작
        stk.push([now, i])

print(" ".join(map(str, res)))