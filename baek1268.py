import sys
sys.stdin = open("baek1268.txt")


N =  int(input())
# 1반부터 9반까지존재 .학년은 1학년부터 5학년까지존재
classes = [[[] for _ in range(0, 10)] for _ in range(0, 6)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))

    for j in range(0, len(tmp)):
        cur_class = tmp[j]

        classes[j+1][cur_class].append(i)

visited = [[False] * (N+1) for _ in range(0, N+1)]
chk_arr = [0] * (N+1)

for i in range(1, 6):
    for j in range(1, 10):
        cur_arr = classes[i][j]

        if len(cur_arr) > 1:
            for k in range(1, len(cur_arr)):
                for l in range(0, k):
                    num1 = cur_arr[k]
                    num2 = cur_arr[l]
                    
                    if not visited[num1][num2]:
                        visited[num1][num2] = True
                        chk_arr[num1] += 1
                    if not visited[num2][num1]:
                        visited[num2][num1] = True
                        chk_arr[num2] += 1

max_cnt = 0
max_student = 1
for i in range(1, N+1):
    if chk_arr[i] > max_cnt:
        max_cnt = chk_arr[i]
        max_student = i
print(max_student)
