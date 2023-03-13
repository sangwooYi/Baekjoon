import sys
sys.stdin = open("baek2841.txt")

"""
줄은 1번부터 6번까지 존재한다.

이때 특정 줄에 존재하는 스택값이 없으면 or 현재 존재하는 가장 높은 값보다 다음에오는게 더 높으면 
=> 바로 push cnt += 1

현재 존재하는 줄에서 가장 높은 스택값보다 낮은 플랫값이 들어오면
=> 현재 입력값보다 낮은값이 나올떄까지 계속 pop 하면서 cnt += 1
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


N, P = map(int, sys.stdin.readline().split())

# 0번은 무시
stack_arr = [0] * 7
for i in range(1, 7):
    stack_arr[i] = Stack(N+500)
a = Stack(100)

cnt = 0
for i in range(0, N):

    a, b = map(int, sys.stdin.readline().split())
    if stack_arr[a].is_empty():
        stack_arr[a].push(b)
        cnt += 1
    else:
        flag = False
        # 현재 스택이 있으면서 peek()값이 현재 입력된 플랫보다 크면 pop + 카운팅
        while not stack_arr[a].is_empty():
            peek_value = stack_arr[a].peek()
            if peek_value > b:
                stack_arr[a].pop()
                cnt += 1
            else:
                if peek_value == b:
                    flag = True
                break
        if not flag:
            cnt += 1
            stack_arr[a].push(b)
print(cnt)