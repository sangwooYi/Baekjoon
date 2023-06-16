import sys
sys.stdin = open("baek15723.txt")


alph_to_idx = {}

# a가 0  z가 25
for i in range(0, 26):
    start_idx = ord("a")
    alph_to_idx[chr(start_idx+i)] = i

INF = 987654321
arr = [[INF] * 26 for _ in range(0, 26)]

N = int(input())

for i in range(0, N):
    s, t, e = input().split()

    s_idx = alph_to_idx[s]
    e_idx = alph_to_idx[e]

    # 방향성!
    arr[s_idx][e_idx] = 1

# 플로이드 와샬
for w in range(0, 26):
    for s_idx in range(0, 26):
        for e_idx in range(0, 26):
            if s_idx == e_idx:
                arr[s_idx][e_idx] = 0
            else:
                arr[s_idx][e_idx] = min(arr[s_idx][e_idx], arr[s_idx][w]+arr[w][e_idx])

M = int(input())
for i in range(0, M):
    s, t, e = input().split()
    s_idx = alph_to_idx[s]
    e_idx = alph_to_idx[e]

    if arr[s_idx][e_idx] >= INF:
        print("F")
    else:
        print("T")