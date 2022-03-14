import sys
sys.stdin = open("baek9012.txt")
"""
괄호검사 전형적인 스택문제
( 는 일단 push
) 가 나오면 현재 스택이 비어있으면 => 거짓
스택이 있으면 일단 ( 가 있단 소리 따라서 pop()
(만약 괄호가 여러종류 혼용된 상태라면 pop된 애가 내가 원한건지도 체크 해야함)
다 체크하고나서stk 이 남아있으면 안 된다.
위 조건을 모두 통과해야 VPS (Valid Parenthesis String)
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


def is_right(brackets, n):
    answer = [0] * n
    for i in range(0, n):
        stk = Stack(50)
        flag = True
        for idx in range(0, len(brackets[i])):
            if brackets[i][idx] == "(":
                stk.push(brackets[i][idx])
            elif brackets[i][idx] == ")":
                if stk.is_empty():
                    flag = False
                    answer[i] = "NO"
                    break
                stk.pop()
        if flag:
            if stk.is_empty():
                answer[i] = "YES"
            else:
                answer[i] = "NO"
    return answer


N = int(input())
MAP = [0] * N
for i in range(0, N):
    temp = list(input())
    MAP[i] = temp

ans = is_right(MAP, N)
for i in range(0, N):
    print(ans[i])