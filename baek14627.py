import sys
sys.stdin = open("baek14627.txt")

"""
함정이 있는 문제!
이런 문제를 조심 하자
"""

S, C = map(int, sys.stdin.readline().split())

onions = [0] * S
for i in range(0, S):
    cur = int(sys.stdin.readline().rstrip())
    onions[i] = cur

left = 1
right = 1000000001

while left < right:
    mid = (left+right)//2

    total_cnt = 0
    for onion in onions:
        cur_cnt = onion//mid
        total_cnt += cur_cnt
    # 조각이 많이나온거니까 더 크게 썬다
    if total_cnt >= C:
        left = mid + 1
    # 조각이 적게나온거니까 더 작게 썬다
    else:
        right = mid
greed_len = left-1
answer = 0
# 최대 C개만큼만 쓰면 된다.
cnt = 0
for onion in onions:
    # 이미 조건 충족 더 쓸 필요 X 파닭당 최대 1번 넣을 수 있음
    if cnt >= C:
        answer += onion
    else:
        res_len = onion%greed_len
        cur_max_cnt = onion//greed_len
        
        res_amount = C-cnt
        if res_amount >= cur_max_cnt:
            answer += res_len
            cnt += cur_max_cnt
        else:
            cnt += res_amount
            answer += (res_len + (greed_len*(cur_cnt-res_amount)))

print(answer)
