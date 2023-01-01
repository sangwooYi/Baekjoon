import sys
sys.stdin = open("baek3078.txt")


"""
등수대로 주어지는게 포인트!
(아니면 그냥 사실 정렬하면 끝이긴 함)

1. 일단 현재 길이에 해당하는 큐를 체크
=> 큐에 data가 있다면, que의 top 에 있는 값의 (peek) 등수 - 현재 학생의 등수 > K 인 조건을 전부 제거
=> 그 후에 현재 que에 남아있는 data 만큼이 현재 학생과 좋은 친구 쌍인것
=> 현재 학생을 해당 que에 추가 
이걸 첫번째 학생부터 마지막 학생까지 진행
"""

class Queue:
    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.front = 0
        self.rear = 0
        self.data = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.rear += 1
        self.data += 1

        if self.rear == self.max:
            self.rear = 0
        return x

    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.front += 1
        self.data -= 1

        if self.front == self.max:
            self.front = 0
        return now

    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.data

    def is_empty(self):
        return self.data <= 0


N, K = map(int, sys.stdin.readline().split())
friends = [0] * N
que_list = [Queue(N*2) for _ in range(0, 21)]

cnt = 0
for i in range(0, N):
    name_len = len(sys.stdin.readline().rstrip())
    friends[i] = name_len

    while not que_list[name_len].is_empty() and (i - que_list[name_len].peek()) > K:
        que_list[name_len].dequeue()
    
    if not que_list[name_len].is_empty():
        cnt += que_list[name_len].size()
    que_list[name_len].enqueue(i)
    

print(cnt)

