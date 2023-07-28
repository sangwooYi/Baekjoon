import sys
sys.stdin = open("baek2851.txt")

arr = [0] * 10
for i in range(0, 10):
    arr[i] = int(input())

sum_arr = [0] * 10
sum_arr[0] = arr[0]
for i in range(1, 10):
    sum_arr[i] = sum_arr[i-1]+arr[i]

ans = 0
# j부터 i 까지
for i in range(0, 10):
    cur_sum = sum_arr[i]
    
    cur_abs = abs(cur_sum-100)
    ans_abs = abs(ans-100)
    if cur_abs <= ans_abs:
        ans = cur_sum
print(ans)
            