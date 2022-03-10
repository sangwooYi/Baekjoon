import sys
sys.stdin = open("baek10828.txt")


class Stack:
    def __init__(self, capacity):
        self.max = capacity
        self.ptr = 0
        self.data = 0
        self.stk = [0] * self.max

    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.ptr += 1
        self.data += 1
        return x

    def pop(self):
        if self.data <= 0:
            return -1
        self.ptr -= 1
        now = self.stk[self.ptr]
        self.data -= 1
        return now
    
    def size(self):
        return self.data

    # 비어있으면 1 아니면 0
    def empty(self):
        if self.data <= 0:
            return 1   
        return 0
    
    def top(self):
        if self.data <= 0:
            return -1
        # 값만 확인하고 얘는 빼지는 않는다
        now = self.stk[self.ptr-1]
        return now

def baek10828(commands, n):
    stk = Stack(n+10)
    answer = []
    for i in range(0, n):
        command = commands[i]
        if command[0] == "push":
            stk.push(int(command[1]))
        elif command[0] == "pop":
            temp = stk.pop()
            answer.append(temp)
        elif command[0] == "size":
            temp = stk.size()
            answer.append(temp)
        elif command[0] == "empty":
            temp = stk.empty()
            answer.append(temp)
        elif command[0] == "top":
            temp = stk.top()
            answer.append(temp)
    return answer


N = int(input())
CDS = [0] * N
for i in range(0, N):
    CDS[i] = input().split()

ans = baek10828(CDS, N)
for i in range(0, len(ans)):
    print(ans[i])