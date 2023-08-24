import sys
sys.stdin = open("baek2217.txt")


N = int(sys.stdin.readline().rstrip())
ropes = [0] * N
for i in range(0, N):
    ropes[i] = int(sys.stdin.readline().rstrip())

ropes.sort()
answer = 0
for i in range(0, N):
    cur_weight = ropes[i]

    tmp_total = cur_weight*(N-i)
    answer = max(answer, tmp_total)
print(answer)