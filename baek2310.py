import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek2310.txt")


"""
E: 빈방
L: 레프리콘
T: 트롤

얘는 DFS가 오히려 더 편할 듯
"""

def is_possible(node, cash, room_info, graph):

    global answer

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        next_code, next_cost = room_info[next_node]

        if next_code == "T":
            if cash < next_cost:
                continue
            next_cash = cash-next_cost
        elif next_code == "L":
            if cash <= next_cost:
                next_cash = next_cost
            else:
                next_cash = cash
        else:
            next_cash = cash
        
        if next_node == N:
            answer = "Yes"
            return
        visited[next_node] = True
        is_possible(next_node, next_cash, room_info, graph)
        visited[next_node] = False

while True:
    N = int(input())
    # 종료 조건
    if N == 0:
        break

    room_info = [0] * (N+1)
    graph = [[] for _ in range(0, N+1)]
    for i in range(0, N):
        tmp = list(input().split())

        code = tmp[0]
        cost = int(tmp[1])
        nodes = list(map(int, tmp[2:-1]))

        # 각 방의 타입과, 금액을 저장
        room_info[i+1] = (code, cost)
        
        for node in nodes:
            graph[i+1].append(node)
        
    visited = [False] * (N+1)
    visited[1] = True

    start_code, start_cost = room_info[1]
    
    answer = "No"

    # 시작부터 트롤방이면 진행 X
    if start_code != "T":

        if start_code == "L":
            start_cash = start_cost
        else:
            start_cash = 0
        # 노드, 소지금
        is_possible(1, start_cash, room_info, graph)
    print(answer)