import sys
sys.stdin = open("baek1167.txt")

"""
기본적으로 단방향 그래프인듯?
정점갯수가 10만개까지. 완전탐색은 택도없다
최악의 경우 한 노드에 대한 탐색 수가 10만 x 10먄 

"""

V = int(sys.stdin.readline())
G = [[] for _ in range(0, V+1)]
for i in range(0, V):
    temp = list(map(int, sys.stdin.readline().split()))
    node = temp[0]
    # len(temp) - 3까지만 탐색
    for j in range(1, len(temp)-2, 2):
        G[node].append((temp[j], temp[j+1]))
