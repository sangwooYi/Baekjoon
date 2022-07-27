import sys
sys.stdin = open("baek14867.txt")


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
    
    def is_empty(self):
        return self.data <= 0


a_max, b_max, a_goal, b_goal = map(int, input().split())

que = Queue(1000000)
# 중복 방지
check_dict = {}
check_dict[(0, 0)] = 1

que.enqueue((0, 0, 0))

"""
총 6가지 행동을 할 수있다.
A 가득채우기 , B 가득채우기
A 비우기, B 비우기
A -> B로 붓기,  B -> A로 붓기
"""
INF = 987654321
answer = INF
while not que.is_empty():
    a_now, b_now, cnt = que.dequeue()
    if a_now == a_goal and b_now == b_goal:
        answer = cnt
        break
    # F(x)
    if a_now < a_max:
        a_next = a_max
        b_next = b_now
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))
    if b_now < b_max:
        a_next = a_now
        b_next = b_max
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break        
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))
    
    if a_now > 0:
        # E(x)
        a_next = 0
        b_next = b_now
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break        
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))
        # M(x, y) A => B로
        if a_now + b_now <= b_max:
            a_next = 0
            b_next = a_now + b_now
        else:
            a_next = a_now - (b_max-b_now)
            b_next = b_max
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break        
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))        
    if b_now > 0:
        # E(x)
        a_next = a_now
        b_next = 0
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break        
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))
        # M(x, y) B => A 로 
        if a_now + b_now <= a_max:
            a_next = a_now + b_now
            b_next = 0
        else:
            a_next = a_max
            b_next = b_now - (a_max - a_now)
        if a_next == a_goal and b_next == b_goal:
            answer = cnt+1
            break        
        if (a_next, b_next) not in check_dict.keys():
            check_dict[(a_next, b_next)] = 1
            que.enqueue((a_next, b_next, cnt+1))        

if answer == INF:
    answer = -1
print(answer)