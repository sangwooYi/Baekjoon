"""
.sort(key=lambda x: 정렬기준)
이거 너무 편하다.. 꼭 기억하자
"""

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
MAP.sort(key=lambda x: (x[1], x[0]))
for i in range(0, N):
    print(MAP[i][0], end=" ")
    print(MAP[i][1])