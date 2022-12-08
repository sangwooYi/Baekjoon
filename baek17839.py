import sys
from collections import deque
sys.stdin = open("baek17839.txt")

"""
문제를 잘읽자!
A 가 다시 A가될 경우가 없다는것이지

A -> B
A -> C
이렇게 
"""


start_node = "Baba"
char_to_idx = {}
idx_to_char = {}
N = int(sys.stdin.readline())
graph = [[] for _ in range(0, N)]
start_idx = -1
for i in range(0, N):

    A, TO, B = sys.stdin.readline().split()
    if A not in char_to_idx.keys():
        # A는 B로 연결된다는걸 의미
        graph[i].append(B)
        char_to_idx[A] = i
        idx_to_char[i] = A
        if A == start_node:
            start_idx = i
    # A가 중복해서 등장할수도있다..    
    else:
        idx = char_to_idx[A]
        graph[idx].append(B)

# Baba명령이 존재할때만
if start_idx != -1:
    answer_dict = {}
    visited = [False] * N
    idx = start_idx
    que = deque()
    visited[start_idx] = True
    que.append(start_node)

    while que:
        now_node = que.popleft()
        
        now_idx = char_to_idx[now_node]
        
        for next_node in graph[now_idx]:
            # 중복 발생 가능
            answer_dict[next_node] = 1
            if next_node not in char_to_idx.keys():
                continue
            next_idx = char_to_idx[next_node]
            if not visited[next_idx]:
                visited[next_idx] = True
                que.append(next_node)
    answer = list(answer_dict.keys())
    answer.sort()
    for i in range(0, len(answer)):
        print(answer[i])
