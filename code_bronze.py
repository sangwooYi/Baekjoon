from audioop import mul


N = int(input())
for i in range(0, N):
    for j in range(0, N-i-1):
        print("", end=" ")
    for j in range(0, i+1):
        print("*", end="")
    print()


NUMS = list(map(int, input().split()))
sum = 0
for i in range(0, len(NUMS)):
    sum += (NUMS[i]**2)
answer = sum % 10
print(answer)  


NUMS = [0] * 9
for idx in range(0, 9):
    num = int(input())
    NUMS[idx] = (num, idx+1)
NUMS.sort(key=lambda x: x[0])
answer = NUMS[-1]
print(answer[0])
print(answer[1])



A = int(input())
B = int(input())
C = int(input())
multi_num = A * B * C
count = [0] * 10
for_iterate = str(multi_num)
for i in range(0, len(for_iterate)):
    digit = int(for_iterate[i])
    count[digit] += 1
for i in range(0, len(count)):
    print(count[i])