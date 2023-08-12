#N, B = map(int, input().split())
N, B = 60466175, 36

digit = {}

alpha = ord("A")
# N 진법이면 N-1 까지 표현되어야 함
for i in range(0, B):
    if i < 10:
        digit[i] = str(i)
    else:
        cur_ascii = alpha+i-10
        digit[i] = chr(cur_ascii)

ans = ""
num = N
while num > 0:
    
    res = num%B
    num = num//B
    cur_digit = digit[res]
    ans = cur_digit + ans
print(ans)
    