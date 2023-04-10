import sys
sys.stdin = open("baek1138.txt")

N = int(input())
in_arr = list(map(int, input().split()))
answer = [0] * N

for i in range(0, N):
    num = in_arr[i]
    
    cnt = 0
    for j in range(0, N):
        if answer[j]:
            continue
        if cnt == num:
            answer[j] = (i+1)
            break
        cnt += 1
print(" ".join(map(str, answer)))