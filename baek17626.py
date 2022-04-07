import sys
sys.stdin = open("baek17626.txt")
"""
그리디 응용?

남은 숫자기준으로 루트 후 버림한 값이 출발점!
그때부터 1이될떄까지 for문돌리면서 BFS 계속 진행
먼저 도착한애가 승리! (DP에 저장하며 중복값 제거  )

DP를 어케써야되냐 ㅡㅡ?
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


def find_min(n, dic):
    que = Queue(n*n)
    # DP 통해 중복 제거
    DP[n] = 0
    que.enqueue((n, 0))

    while not que.is_empty():
        now = que.dequeue()
        num = now[0]
        path = now[1]
        start = int(num **(1/2))
        # start부터 1까지 순회
        for i in range(start, 0, -1):
            # start제곱과의 차이
            next_num = num - (dic[i])
            if next_num == 0:
                return path+1
            # 현재 진행하려는게 기존 저장값보다 크면 pass
            if DP[next_num] <= path+1:
                continue 
            DP[next_num] = path+1
            que.enqueue((next_num, DP[next_num]))


N = int(input())
root = int(N**(1/2))
INF = 987
DP = [987] * 50001
sqr_dict = {}
# 일단 한번 저장
for i in range(1, root+1):
    DP[i**2] = 1
    sqr_dict[i] = i**2
ans = find_min(N, sqr_dict)
print(ans)