import sys
sys.stdin = open("baek1208.txt")

"""
연속되지 않은 경우도 부분 수열이라고 본다!
다시 풀어볼 것
부분수열 합의 모든경우를 구하는 한계범위는 N이 20까지임!
따라서 아이디어는
1. 총 40개의 수열을 20 / 20개로 쪼갠다
2. 두 파트의 부분 수열합을 각각 전부 구한다. 2**20 ~== 100만이므로 충분히 가능
3. 첫번째 부분합수열은 오름차순, 두번째 부분합 수열은 내림차순으로 정렬
4. 그 뒤 투포인터 알고리즘을 사용한다. 
=> 만약 두 부분수열 합의 합이 S보다 작으면, 첫번째 part 포인터를 1 증가 (더 키워주어야 하므로)
   반대로 크면 두번째 part의 포인터를 1증가 (더 줄어야 하므로)
   같은 값이면 현재 포인터 기준 첫뻔쨰 part, 두번째 part를 각각 움직이며
   다음 부분합수열에서 같은 값이 있는지 체크 (경우의 수가 고려 되는것)
5. 두 파트 모두 공집합인 경우가 한가지 있으므로, S가 0이면 1 빼주어야 함
"""


N, S = map(int, input().split())
nums = list(map(int, input().split()))

m = N//2
n = N-m
# 총 2**m의 경우가 존재
first = [0] * (1<<n)
second = [0] * (1<<m)

for i in range(0, 1<<n):
    for k in range(0, n):
        # 비트가 겹치는 경우면 합산 1010 이면 2번째, 4번째의 부분합인것
        if (i & (1<<k)) > 0:
            first[i] += nums[k]
for i in range(0, 1<<m):
    for k in range(0, m):
        if (i & (1<<k)) > 0:
            second[i] += nums[k+n]

# 첫 부분은 오름차순
first.sort()

# 두번째 부분은 내림차순
second.sort(key=lambda x : -x)


f_len = (1<<n)
s_len = (1<<m)
fp = 0
sp = 0  
answer = 0
while fp < f_len and sp < s_len:
    tmp_sum = first[fp] + second[sp]

    # S 가 나온다면, 혹시 연속되게 같은 값이 있는지도 체크해 주어야함 (경우의 수)
    if tmp_sum == S:
        c1 = 1
        c2 = 1
        fp += 1
        sp += 1
        # 인접한 부분합중 같은 값이 있는지 체크
        while fp < f_len and first[fp] == first[fp-1]:
            c1 += 1
            fp += 1
        while sp < s_len and second[sp] == second[sp-1]:
            c2 += 1
            sp += 1
        answer += (c1*c2)

    # 첫번째 파트는 오름차순, 두번쨰 파트는 내림차순이므로
    # 만약 S보다 작은 합이면 첫번째 파트를 1 증가시킨다.
    elif tmp_sum < S:
        fp += 1
    
    # 위와 같은로직으로 S보다 큰 부분합이면 두번쨰파트를 1 감소시킨다.
    else:
        sp += 1
# 공집합인 경우를 따져주어야함
if S == 0:
    answer -= 1
print(answer)