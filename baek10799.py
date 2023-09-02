S = list(input())


stk = []

# 레이저 나올때마다 카운팅
#

total_cnt = 0
lazer_idx = 0
for i in range(0, len(S)):
    if S[i] == "(":
        stk.append(lazer_idx)
    else:
        # 스택에있는거 빼기
        cur_idx = stk.pop()

        # 레이저
        if lazer_idx == cur_idx:
            lazer_idx += 1
        else:
            total_cnt += (lazer_idx-cur_idx+1)
print(total_cnt)