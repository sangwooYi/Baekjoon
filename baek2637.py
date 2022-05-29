import sys
sys.stdin = open("baek2637.txt")

"""
위상정렬이 필요한 case
그래프에서 현재 노드에서, 다음 노드로 가기위해서
현재 노드로 진입한 이전 노드들을 선행적으로 모두 거친 이후여야 하는 경우

ex)  3번노드에 1,2 노드가 연관되어있고 3번노드가 4번노드로 연결되어있는상태에서
3번노드가 4번노드로 진행 가능한 조건이
그 전에 1,2노드가 모두 3번노드로 들어온 이후 일 때!


이 문제에서 point
초기 시작점 == 기본 부품,
기본 부품 => 중간부품 일때는 해당 기본부품 만큼 + 
중간부품 => 중간부품 일때는 중간부품에서의 기본부품 요소들 * 중간부품 갯수 (즉 곱하기)

따라서 중간부품의 경우, 
중간부품에 필요한 기본부품들 갯수에 대한 정보를 담고있어야 한다.
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



# N은 완제품 번호, 즉 N이 도착지점이 되는 것 
N = int(input())
M = int(input())
graph = [[] for _ in range(0, N+1)]
in_degree = [0] * (N+1)
# X Y Z   X <- Y 로 Z만큼 cost가 필요하다는 의미
for i in range(0, M):
    # y -> x 로 가는데 필요한 cost가 z인것
    x, y, z = map(int, input().split())
    # 노드 방향과 cost 저장
    graph[y].append((x, z))
    # 진입 차수 (해당 노드로 들어오는 노드들의 갯수 체크)
    in_degree[x] += 1


que = Queue(N*N*100)

cost = [0] * (N+1)
base_part = []

# 중간 부품에서 필요한 기본부품들 갯수를 저장
midpart_num = {}
# 현재 진입차수가 0인애들을 전부 체크(이 노드로 들어오는애들이 없으므로 시작점인것)
# 여기서 in_degree[i] == 0인애들이 기본 부품인것
for i in range(1, N+1):
    if in_degree[i] == 0:
        # 기본부품 
        base_part.append(i)
        # 노드를 큐에 저장
        que.enqueue(i)

# 중간 부품에 대한 dict 생성 (기본 부품들을 얼마나 사용하는지에 대한 정보를 갖고 있다.)
for i in range(1, N+1):
    if in_degree[i] > 0:
        midpart_num[i] = {}
        for j in range(0, len(base_part)):
            midpart_num[i][base_part[j]] = 0


while not que.is_empty():
    node = que.dequeue()

    for next_node, next_cost in graph[node]:
        # 간선 제거
        in_degree[next_node] -= 1
        # 현재 노드가 기본부품에서부터 온거면
        if node in base_part:
            # 중간부품에서 기본부품 필요한 갯수만큼 + (중간부품 구성 요소를 만드는것)
            midpart_num[next_node][node] += next_cost
        # 현재 노드가 중간부품인 경우, 위상정렬이므로, 이미 구성요소에 대한 카운팅은 끝난 상태
        else:
            for k in range(0, len(base_part)):
                # 다음 중간부품을 만드는데 필요한 기본부품 갯수를 카운팅
                midpart_num[next_node][base_part[k]] += (next_cost*midpart_num[node][base_part[k]])

        # 진입 관련 간선이 전부 제거되었을 경우에만 다음단계로 진행 가능
        if in_degree[next_node] == 0:
            que.enqueue(next_node)

result = midpart_num[N]
base_part.sort()
for i in range(0, len(base_part)):
    node = base_part[i]
    cost = result[node]
    print(f"{node} {cost}")