import sys
sys.stdin = open("baek11650.txt")

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
MAP.sort(key=lambda x: (x[0], x[1]))
for i in range(0, N):
    print(MAP[i][0], end=" ")
    print(MAP[i][1])