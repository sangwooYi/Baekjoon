import sys
sys.stdin = open("baek18113.txt")



"""
꼬다리 양쪽을 K 씩 짜른다
만약 길이가 < 2K면 한쪽만 짜르고
<= K 면 폐기
"""
N, K, M = map(int, sys.stdin.readline().split())
gims = [0] * N
cnt = 0
for i in range(0, N):
    cur_len = int(sys.stdin.readline().rstrip())

    if cur_len <= K:
        continue
    if cur_len < 2*K:
        gims[i] = cur_len-K
        cnt += 1
    else:
        gims[i] = cur_len-2*K
        if gims[i]:
            cnt += 1
if cnt == 0:
    print(-1)

else:
    left = 0
    right = 1000000001

    while left < right:
        mid = (left+right)//2
        if mid == 0:
            break
        cur_cnt = 0
        for i in range(0, N):
            # 길이가 있는 경우만
            if gims[i]:
                cur_cnt += (gims[i]//mid)
        if cur_cnt >= M:
            left = mid+1
        else:
            right = mid
    print(left-1)
