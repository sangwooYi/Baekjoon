N = input()

check_arr = [0] * 10

for i in range(0, len(N)):
    num = int(N[i])

    if num == 9:
        if check_arr[6] < check_arr[9]:
            check_arr[6] += 1
        else:
            check_arr[9] += 1
    elif num == 6:
        if check_arr[9] < check_arr[6]:
            check_arr[9] += 1
        else:
            check_arr[6] += 1
    else:
        check_arr[num] += 1
print(max(check_arr))