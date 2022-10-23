N = int(input())
answer = 0
for i in range(1, N+1):
    digit = list(map(int, str(i)))
    if len(digit) <= 2:
        answer += 1
    else:
        term = digit[1]-digit[0]
        flag = True
        for i in range(2, len(digit)):
            if digit[i] - digit[i-1] != term:
                flag = False
                break
        if flag:
            answer += 1
print(answer)