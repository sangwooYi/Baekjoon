import sys
sys.stdin = open("baek16120.txt")

"""
그냥 무식하게

stack 기준 
stack에서 ppap 만들어질떄마다 ppap => p 로 

p 하나만 있어도 PPAP 문자열!
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
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def size(self):
        return self.data


    def peek_size(self, size):
        if self.data < size:
            raise IndexError
        ans = [0] * size
        start = self.ptr - size
        idx = 0
        for i in range(start, self.ptr):
            ans[idx] = self.stk[i]
            idx += 1
        return ans

    def is_empty(self):
        return self.data <= 0


array = list(sys.stdin.readline().rstrip())
if len(array) < 4:
    if len(array) == 1 and array[0] == "P":
        print("PPAP")
    else:
        print("NP")
    
else:
    stk = Stack(len(array)+10)
    check = ["P", "P", "A"]

    for i in range(0, len(array)):
        now = array[i]
        # stk.size가 3 미만이면 굳이 볼필요도 없다
        if now == "P" and stk.size() >= 3:
            temp = stk.peek_size(3)
            # PPA가 스택에 쌓이면 없애고 P만 push
            if temp == check:
                for i in range(0, 3):
                    stk.pop()
        stk.push(now)

    if stk.size() == 1:
        tmp = stk.pop()
        if tmp == "P":
            print("PPAP")
    else:
        print("NP")

            

    