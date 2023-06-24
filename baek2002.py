import sys
sys.stdin = open("baek2002.txt")


N = int(input())


check_map = {}
visited = [False] * N
for i in range(0, N):
    in_car = input()

    check_map[in_car] = i


answer = 0

for i in range(0, N):
    out_car = input()

    car_ord = check_map[out_car]

    if not visited[car_ord]:
        visited[car_ord] = True

        flag = True
        for j in range(0, car_ord):
            if not visited[j]:
                flag = False
                break
        if not flag:
            answer += 1
print(answer)