import sys
sys.stdin = open("baek10775.txt")

"""
초기 전략.
현재 노드에서 빈 곳 찾을떄까지 가보는것
=> 시간초과..
해법: 해당 줄에서 가능한 최솟값을 바로 찾을 수 있게 


=> 정식 풀이는 find union으로 푼다!
현재 find(node) 가 0이아닌경우라면 
x = find(node)에서 x가 의미하는것은
현재 도킹 가능한 최소 위치!
x 가 0이 아니라면 따라서
union(x, x-1) (현재 위치를 도킹했다는 처리를 하는것) 그리고 count
현재 find(x) 가 0인경우에 끝내는걸로! 

시간은 내풀이가 더 빠르다!

why? 나는 현재 도킹 가능한 지점을 hash 개념으로 찾았기 때문!
그에비해 find-union은 재귀가 들어가서 오히려 효율성은 뒤진다.
"""


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

waitings = [0] * P
for i in range(0, P):
    waitings[i] = int(sys.stdin.readline())

# 차례대로 도킹해야 한다.
answer = 0

visited = [False] * (G+1)
# i번 대기열에서 탐색 출발지
# 해당 노드 값이 0이거나, 출발지점부터 체크한게 전부 차있다면 끝?
possible = [i for i in range(G+1)]

for i in range(0, len(waitings)):
    node = waitings[i]

    flag = False
    start = possible[node]
    if start == 0:
        break
    for j in range(start, 0, -1):
        if not visited[j]:
            flag = True
            visited[j] = True
            answer += 1
            possible[node] = j-1
            break
    if not flag:
        break
print(answer)


# def find(x):
#     if x == parent[x]:
#         return x
#     px = find(parent[x])
#     parent[x] = px
#     return px

# def union(x, y):
#     px = find(x)
#     py = find(y)
    
#     if px <= py:
#         parent[py] = px
#     else:
#         parent[px] = py

# parent = [i for i in range(0, G+1)]

# answer = 0
# for i in range(0, len(waitings)):
#     node = waitings[i]

#     x = find(node)
#     if x == 0:
#         break
#     union(x, x-1)
#     answer += 1
# print(answer)