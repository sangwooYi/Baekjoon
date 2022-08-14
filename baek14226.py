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
    

"""
어느정도 DP개념까지 포함된 문제풀이!
혼자 풀 수 있어야한다.
"""

def bfs(target):
    que = Queue(1000000)
    DP = [[-1] * (target+1) for _ in range(0, target+1)]
    # DP[i][j]  i라는 숫자를 현재 클립보드 j 상태에서의 만들수있는 최소 시간!
    DP[1][0] = 0
    que.enqueue((1, 0))

    while not que.is_empty():
        num, paste = que.dequeue()
        # 클립보드에 복사
        if DP[num][num] == -1:
            DP[num][num] = DP[num][paste] + 1
            que.enqueue((num, num))
        
        # 붙여넣기
        next_num = num + paste
        if next_num <= target:
            if DP[next_num][paste] == -1:
                DP[next_num][paste] = DP[num][paste] + 1
                que.enqueue((next_num, paste))
        # 1 빼기
        next_num = num - 1
        if next_num >= 0:
            if DP[next_num][paste] == -1:
                DP[next_num][paste] = DP[num][paste] + 1
                que.enqueue((next_num, paste))
    return DP[target]


S = int(input())
temp = bfs(S)
answer = 987654321
for i in range(1, len(temp)):
    if temp[i] == -1:
        continue
    answer = min(answer, temp[i])
print(answer)