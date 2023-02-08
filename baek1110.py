N = int(input())

now = N
cnt = 0
while True:
    cnt += 1
    now_front_num = now//10
    now_rear_num = now%10

    next_sum = now_front_num+now_rear_num
    
    next_num = now_rear_num*10+next_sum%10
    if next_num == N:
        break
    else:
        now= next_num
print(cnt)
