

# N = int(input())
# for i in range(0, N):
#     for j in range(0, N-i-1):
#         print("", end=" ")
#     for j in range(0, i+1):
#         print("*", end="")
#     print()


# NUMS = list(map(int, input().split()))
# sum = 0
# for i in range(0, len(NUMS)):
#     sum += (NUMS[i]**2)
# answer = sum % 10


# NUMS = [0] * 9
# for idx in range(0, 9):
#     num = int(input())
#     NUMS[idx] = (num, idx+1)
# NUMS.sort(key=lambda x: x[0])
# answer = NUMS[-1]
# print(answer[0])
# print(answer[1])



# A = int(input())
# B = int(input())
# C = int(input())
# multi_num = A * B * C
# count = [0] * 10
# for_iterate = str(multi_num)
# for i in range(0, len(for_iterate)):
#     digit = int(for_iterate[i])
#     count[digit] += 1
# for i in range(0, len(count)):
#     print(count[i])


# N = int(input())
# for i in range(1, 10):
#     mult = N*i
#     print(N, "*", i, "=", mult)

N = int(input())
if ((N % 4 == 0) and (N % 100 !=  0)) or N % 400 == 0:
    print(1)
else:
    print(0)


N, M = map(int, input().split())
hour = N
if M >= 45:
    minute = M-45
else:
    sub = (45-M)
    if hour == 0:
        hour = 23
    else:
        hour = N-1
    minute = (60-sub)
print(hour, end=" ")
print(minute)



nums = list(map(int, input().split()))

asc_flag = True
dsc_flag = True
for i in range(0, len(nums)):
    if not asc_flag and not dsc_flag:
        break
    if i+1 != nums[i]:
        asc_flag = False
    if 8-i != nums[i]:
        dsc_flag = False

if asc_flag:
    print("ascending")
elif dsc_flag:
    print("descending")
else:
    print("mixed")