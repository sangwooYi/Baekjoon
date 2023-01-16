import sys
sys.stdin = open("baek2230.txt")


N, M = map(int, sys.stdin.readline().split())
numbers = [0]  *N
for i in range(0, N):
    numbers[i] = int(sys.stdin.readline())
numbers.sort()


start = 0
end = 1

INF = 99999999999

min_sub = INF
while end < N:
    if start == end:
        end += 1
    else:
        now_sub = numbers[end] - numbers[start]

        if now_sub >= M:
            start += 1
            min_sub = min(min_sub, now_sub)
        else:
            end += 1
print(min_sub)