A, B = map(int, input().split())

def make_rev(num):
    str_num = str(num)
    tmp = ""
    for i in range(len(str_num)-1, -1, -1):
        tmp += str(str_num[i])
    return int(tmp)


rev_A = make_rev(A)
rev_B = make_rev(B)
answer = make_rev(rev_A+rev_B)
print(answer)