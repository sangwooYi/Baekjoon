N, M = map(int, input().split())
check_dict = {}
answer = 0

for i in range(0, N):
    now = input()
    check_dict[now] = 1

for i in range(0, M):
    now = input()
    if now in check_dict.keys():
        answer += 1
print(answer)