import sys
sys.stdin = open("baek5430.txt")

"""
앞뒤로 뺴는것만 구현해서 ㄱㄱ
그리고 R 나올떄마다 flag 바꿔서
flag = True(정방향) 앞에서 빼고
flag = Flase(역방향) 뒤에서 뺴고
어떤방향으로 출력할지 결정

sys.stdin.readline()의 경우는 공백이 있는경우 /n 까지 그대로 출력된다.
input() 은 알아서 공백이 없어짐 
따라서 이런 input이 주어지는 경우에는
sys.stdin.readline().rstrip() 을 통해 입력을 받을것!(우측 공백 제거)
"""


class deQueue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0

    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.rear -= 1
        if self.rear == -1:
            self.rear == self.max-1
        now = self.que[self.rear]
        self.data -= 1
        return now
    
    def isEmpty(self):
        return self.data <= 0
    
    def sizeOf(self):
        return self.data


T = int(input())
for tc in range(1, T+1):
    operator = list(input())
    N = int(input())
    ans = "["
    que = deQueue(200000)
    temp = input()[1:-1]
    if N == 0:
        arr = []
    else:
        arr = list(temp.split(","))
    if len(arr) > 0:
        for i in range(0, len(arr)):
            que.enqueue(arr[i])
    # True일때 정방향, False일때 역방향
    flag = True
    is_error = False
    for i in range(0, len(operator)):
        if operator[i] == "R":
            # flag 토글
            if flag:
                flag = False
            else:
                flag = True
        elif operator[i] == "D":
            if que.isEmpty():
                is_error = True
                ans = "error"
                break
            if flag:
                que.dequeue()
            else:
                que.pop()
    if not is_error:
        while not que.isEmpty():
            if flag:
                now = que.dequeue()
                ans += now
                if que.sizeOf() > 0:
                    ans += ","
            else:
                now = que.pop()
                ans += now
                if que.sizeOf() > 0:
                    ans += ","
        ans += "]"
    print(ans)