import sys
sys.stdin = open("baek2568.txt")


"""
A 기준 오름차순 정렬 후,
B 기준 LIS 를 찾으면 됨

근데 내가 지금까지한건 
O(N^2) 의 복잡도를 갖는다. (쉬운 버전)

하지만 O(NlogN) 으로 LIS를 구현하는 알고리즘도 존재!
이걸 기억해두자 
O(NlogN) 의 알고리즘은 이분탐색의 lower bound를 이용함

1. arr[i] <= arr[i+1] 이라면 벡터에 저장
2. arr[i] > arr[i+1] 이라면들어갈 위치를 찾은 후 원소를 대체해 줌
(LIS의 마지막 요소가 작을 수록 LIS를 더 길게 생성할 수 있음)

단 이 방법은 LIS의 '길이' 만 구할 수 있으며, 실제 요소를 체크하려면 추가적인 작업이 필요하다!
(이 부분을 주의하자)
# LIS 원소가 교체 or 들어올때의 해당 요소의 인덱스 값을 체크
# 인덱스 위치를 내림차순으로 정렬한 뒤 요소를 역순으로 뽑아내면,
# 주어진 수열을 역순으로 체크할때의 LDS 가 나온다! 이를 다시 역순으로 돌리면 그게 LIS 요소임!
"""

N = int(sys.stdin.readline())
lines = [0] * N


check = {}
for i in range(0, N):
    # list(map())보다 그냥 이렇게 구조분해 할당하는것이 더 효율적이다!
    # why? list로 변환하는데 또 추가적인 시간이 필요하기 때문!
    a, b = map(int, sys.stdin.readline().split())
    lines[i] = (a, b)
lines.sort()

LIS = [lines[0][1]]
DP = [-1] * N
for i in range(0, N):
    a, b = lines[i]
    # LIS의 마지막요소와 비교하여 LIS가 유지되면 그냥 추가
    if LIS[-1] < b:
        LIS.append(b)
        DP[i] = max(DP)+1
    else:
        # LIS[-1] > b라면 b가 들어갈 적절한 위치를 찾아 요소를 대체해줌
        pl = 0
        pr = len(LIS)-1
        while pl <= pr:
            pc = (pl+pr)//2

            if LIS[pc] >= b:
                pr = pc-1
            else:
                pl = pc+1
        if b > LIS[pl]:
            LIS[-1] = b
        else:
            LIS[pl] = b
            DP[i] = pl+1

print(N-len(LIS))

now = len(LIS)
w = []
r = len(LIS)

for i in range(N-1, -1, -1):
    if r == 0:
        break
    if DP[i] == r:
        w.append(lines[i])
        r -= 1

c = []
for i in range(0, N):
    if lines[i] not in w:
        c.append(lines[i])
c.sort(key=lambda x : x[0])
for i in range(0, N-len(LIS)):
    print(c[i][0])