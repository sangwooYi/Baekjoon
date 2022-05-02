import sys
sys.stdin = open("baek13549.txt")
"""
아 ... 얘는 가중치가 붙어있다 ㅡㅡ;
따라서 다 돌리고나서 체크해보아야함

이동하는 비용이 동일하지 않은경우는 DP 사용할 때 주의하자! 
최소 횟수 != 최소 비용 임을 항상 주의!

동일한 비용이 발생하는 경우에만, 
최소 횟수 == 최소 비용이다!

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
        self.front +=1 
        if self.front == self.max:
            self.front = 0
        return now
    
    def is_empty(self):
        return self.data <= 0
    

def find_min_path(n, k):
    INF = 9876543
    que = Queue(500000)
    upper = 100000
    lower = 0
    DP = [INF] * (upper+1)
    DP[n] = 0
    que.enqueue((n, 0))

    while not que.is_empty():
        point, path = que.dequeue()
        # 필요 없음
        if DP[point] < path:
            continue
        for i in range(0, 3):
            if i == 0:
                next_point = point + 1
                next_path = path+1
                if next_point > upper:
                    continue
            elif i == 1:
                next_point = point - 1
                next_path = path+1
                if next_point < lower:
                    continue
            elif i == 2:
                next_point = point*2
                next_path = path # 순간이동 0초
                if next_point > upper:
                    continue
            if DP[next_point] <= next_path:
                continue
            # 작은값 나올때만 갱신
            DP[next_point] = next_path
            que.enqueue((next_point, next_path))
    return DP[k]


N, K = map(int, input().split())
if K <= N:
    # 무조건 X-1로밖에 갈 수 없다.
    answer = (N-K)
# N > K 인경우만
else:
    answer = find_min_path(N, K)
print(answer)