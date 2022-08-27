import sys
sys.stdin = open("baek12869.txt")

"""
그냥 쉽게 생각하자..
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
    
    def is_empty(self):
        return self.data <= 0

def perm():
    temp = []
    atk = [1, 3, 9]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if i != j and j != k and i != k:
                    temp.append([atk[i], atk[j], atk[k]])
    return temp    


# 1 ~ 3 임.. 무조건 길이 3으로 맞추는게 센스임.
N = int(input())
SCV = list(map(int, input().split()))
SCV += ([0] * (3-N))
visited = [[[False] * 61 for _ in range(0, 61)] for _ in range(0, 61)]

visited[SCV[0]][SCV[1]][SCV[2]] = True
que = Queue(200000)
que.enqueue((SCV, 0))

cases = perm()
answer = 0
while not que.is_empty():
    tmp, time = que.dequeue()
    flag = True
    for i in range(0, 3):
        if tmp[i] != 0:
            flag = False
            break
    if flag:
        answer = time
        break
    for case in cases:
        next_scv = [0] * 3
        for i in range(0, 3):
            n_scv = tmp[i] - case[i]
            if n_scv < 0:
                n_scv = 0
            next_scv[i] = n_scv

        if visited[next_scv[0]][next_scv[1]][next_scv[2]]:
            continue
        visited[next_scv[0]][next_scv[1]][next_scv[2]] = True
        que.enqueue([next_scv, time+1])

print(answer)