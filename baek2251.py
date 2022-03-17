import sys
sys.stdin = open("baek2251.txt")

"""
컵이 3개뿐이므로 DFS도 가능하나 중복이 발생한다는점에서
BFS 풀이가 더 바람직하다!
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
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear == 0
        return x

    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.rear == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


# cup1에 있는걸 cup2로 붓는 경우 이동량을 return
def fill_up(cup1, key, cup2):
    if cup1 == 0:
        return 0
    # 더 부을수 있는 양이 a의 양 이상인 경우
    if (DICT[key]-cup2) >= cup1:
        return cup1
    # (B-b) < a
    return DICT[key] - cup2


def dfs(now):
    a, b, c = now
    if now in checked:
        return
    checked.append(now)
    # a -> b
    ab = fill_up(a, "b", b)
    next = (a-ab, b+ab, c)
    dfs(next)

    # a -> c
    ac = fill_up(a, "c", c)
    next = (a-ac, b, c+ac)
    dfs(next)

    # b -> a
    ba = fill_up(b, "a", a)
    next = (a+ba, b-ba, c)
    dfs(next)

    # b -> c
    bc = fill_up(b, "c", c)
    next = (a, b-bc, c+bc)
    dfs(next)

    # c -> a
    ca = fill_up(c, "a", a)
    next = (a+ca, b, c-ca)
    dfs(next)

    # c -> b
    cb = fill_up(c, "b", b)
    next = (a, b+cb, c-cb)
    dfs(next)

    if a == 0:
        if c not in case:
            case.append(c)

## BFS로도 가능
def pour(a, b):
    if not visited[a][b]:
        visited[a][b] = True
        que.enqueue((a, b))


# BFS에다가 visited까지 체크하므로 얘는 중복되는 경우를 또 만나지는 않는다!
def BFS():
    while not que.is_empty():
        temp = que.dequeue()
        a = temp[0]
        b = temp[1]
        # 총량이 일정하다는걸 활용!
        c = C - (a+b)
        if a == 0:
            case.append(c)
        # 총 6가지 경우다 전부 체크! (어차피 한쪽이 0이면 변화 없는것)    
        # a -> b
        water = min(a, B-b)
        pour(a-water, b+water)

        # a -> c
        water = min(a, C-c)
        pour(a-water, b)

        # b -> a
        water = min(A-a, b)
        pour(a+water, b-water)

        # b -> c
        water = min(b, C-c)
        pour(a, b-water)

        # c -> a
        water = min(A-a, c)
        pour(a+water, b)

        # c -> b
        water = min(B-b, c)
        pour(a, b+water)


# 전역 상수 처리
A, B, C = map(int, input().split()) 
DICT = {"a": A, "b": B, "c": C}
checked = []
# visited[a][b]  A 물컵과 B물컵의 경우의 수를 저장 (물의 총량은 일정하므로 3개 컵중에서 2개컵만 경우따져도 된다!)
visited = [[False] * (B+1) for _ in range(0, A+1)]
visited[0][0] = True
que = Queue(A*B)
que.enqueue((0, 0))
case = []
BFS()
# dfs((0, 0, C))
case.sort()
for i in range(0, len(case)):
    if i == len(case) - 1:
        print(case[i])
    else:
        print(case[i], end=" ")