import sys
sys.stdin = open("baek2141.txt")

"""
누적합이 전체 인구의 절반이 넘어가는 지점!

전체 인구가 Total 이고,
i-1번쨰에서 i번쨰로 이동할 떄
각 사람간의 거리의 값은
S[i] 는 i까지의 누적합                     
|pos[i]-pos[i-1]| * (+S[i-1] - (total-S[i-1]) 이다!

ex)  A1 = (-1, 3)    A2 = (3, 2)    A3 = (4, 2)  인경우
A1 -> A2로 옮길때 거리합의 변화는   (3-(-1)) * (+3  - (2+2)) 이고,
A2 -> A3로 옮길때 거리합의 변화는  (4-3) * ((3+2) - 2)  가 되는것 !
따라서 2*S[i] - total 이 0보다 처음 커지기 직전의 값이 최소 거리합을 만들어주는 위치가 되는것
S[i] > total // 2
근데 가능한 최소 위치를 찾으라 하였으므로, 거꾸로 탐색!
"""

N = int(input())
MAP = [0] * N

total_cnt = 0
for i in range(0, N):
    pos, cnt = map(int, input().split())
    total_cnt += cnt
    MAP[i] = (pos, cnt)
MAP.sort()


answer = MAP[0][0]
if total_cnt:
    count = 0
    # 가능한 경우가 여러가지라면, 최대한 작은 위치를 출력하기 위함
    for i in range(N-1, -1, -1):
        pos, cnt = MAP[i]
        answer = pos
        count += cnt
        if count > (total_cnt//2):
            break
print(answer)
