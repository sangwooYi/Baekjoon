import sys
sys.stdin = open("baek9019.txt")

"""
아이디어1.
큐를이용해서 계속 4가지 연산을 돌린다.
DP[n] 으로 해당 숫자를 갈 수 있는 최소한의 연산수를 저장

자릿수 변경할때 str / int 변경으로 해도 되지만, 이 과정에서 비용이 많이든다.
따라서 아래처럼 숫자 자체를 이용해서 만들 수 있어야한다!

패턴을 발견하자!
"""


class Queue:

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
        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def isEmpty(self):
        return self.data <= 0

def operD(num):
    res = num * 2
    if res > 9999:
        return (res % 10000)
    return res

def operS(num):
    res = num - 1
    if res < 0:
        return 9999
    return res

# operL, operR을 일단 효율화
# 천의자리를 맨 끝으로 놓고, 나머지는 한자리씩 앞으로 댕기는것
def operL(num):   
         # 이게 백의자리 ~ 일의자리까지 얘네를 한칸씩 앞으로 이동,  뒤에는 천의자리 숫자.
    res = (num % 1000) * 10 + (num // 1000)
    return res

# 일의자리 숫자를 맨 앞으로, 나머지는 한자리씩 오른쪽으로 내린다.
def operR(num):
         # 일의자리숫자를 맨앞으로, 천의자리 ~ 십의자리까지는 한칸씩 뒤로 이동 
    res = (num % 10) * 1000 + (num // 10)
    return res

T = int(input())
for tc in range(0, T):
    A, B = map(int, input().split())
    answer = ""
    if A != B:
        visited = [False] * 10000
        que  = Queue(10000)
        # 오른쪽에 연산수 저장
        que.enqueue((A, ""))
        visited[A] = True
        operator = ["D", "S", "L", "R"]
        while not que.isEmpty():
            now = que.dequeue()
            num = now[0]
            oper = now[1]
            if num == B:
                answer = oper
                break
            for i in range(0, len(operator)):
                if operator[i] == "D":
                    next_num = operD(num)
                    next_oper = oper + "D"
                    # 왠만하면 큐 줄이자, 같아도 pass
                elif operator[i] == "S":
                    next_num = operS(num)
                    next_oper = oper + "S"
                elif operator[i] == "L":
                    next_num = operL(num)
                    next_oper = oper + "L"
                elif operator[i] == "R":
                    next_num = operR(num)
                    next_oper = oper + "R"
                if visited[next_num]:
                    continue
                visited[next_num] = True
                que.enqueue((next_num, next_oper))
        
    print(answer)


