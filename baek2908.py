N, M = map(int, input().split())
# 무조건 세자리숫자 비교이므로  
a = N
b = M
ans = 0
for i in range(0, 3):
    a_mod = a % 10
    b_mod = b % 10
    if a_mod > b_mod:
        ans = N
        break
    elif a_mod < b_mod:
        ans = M
        break
    # 나머지가 같은경우는 판단 불가
    a = a // 10
    b = b // 10
answer = str(ans)
for i in range(len(answer)-1, -1, -1):
    if i == 0:
        print(answer[i])
    else:
        print(answer[i], end="")
    