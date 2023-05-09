class Stack:

    def __init__(self, capacity):
        # 결국 클래스이므로 여기있는 필드들 인스턴스가 쓸수 있다!
        self.max = capacity
        self.stk = [0] * self.max
        self.ptr = 0
        self.data = 0

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
        self.data -= 1
        self.ptr -= 1
        now = self.stk[self.ptr]

        return now
    
    def size(self):
        return self.data
    

    def is_empty(self):
        return self.data <= 0
    
S = input()
T = list(input())


stk = Stack(len(S)+100)

for s in S:
    stk.push(s)

    if not stk.is_empty():

        # 가장 top쪽에 len(T)만큼이 T와 동일한 경우
        if stk.size() >= len(T) and stk.stk[stk.ptr-len(T):stk.ptr] == T:
            
            for i in range(0, len(T)):
                stk.pop()

print("".join(map(str, stk.stk[:stk.ptr])))
    