import sys
sys.stdin = open("baek12015.txt")

"""
LIS를 nlogn 으로 탐색하는 방법

현재 LIS 마지막 인덱스 값보다 큰 값이면 그냥 append
이하의 값이 들어오면 lower bound로 LIS에서 현재 값 이상의 값이 나오는 '처음'위치를 찾아 교체

lower bound: 찾으려는 값 '이상' 값이 처음 나오는 위치 (따라서 찾으려는 값(arr[pc] == key)이 나와도 pr = pc - 1로 갱신)
lower bound: 찾으려는 값보다 '큰'값이 처음 나오는 위치 (따라서 찾으려는 값이 나와도 pl = pc + 1로 갱신)


def lower_bound(arr, key):
    pl = 0
    pr = len(arr)-1

    while pl < pr:
        pc = (pr + pl) // 2
        if arr[pc] >= key:
            pr = pc
        else:
            pl = pc + 1
    return pl

# 따라서 upper bound에서 [찾아진 값에서 하나 작은 위치가 내가 찾으려는 값이 나오는 마지막 위치]
def upper_bound(arr, key):
    pl = 0
    pr = len(arr)-1

    while pl < pr:
        pc = (pr + pl) // 2
        if arr[pc] > key:
            pr = pc
        # 찾으려는 값이 나오더라도 pl 을 pc+1로 갱신 (찾으려는 값보다 큰값이 처음 나오는 위치를 체크해야 하므로)
        else:
            pl = pc + 1
    return pl

# 일반적인 이진 탐색 (그냥 찾으려는 값이 나오기만 하면 되는 것)
def binary_search(arr, key):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        # 찾았으면 바로 해당 위치 반환
        if arr[pc] == key:
            return pc
        elif arr[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
    # 못 찾은것
    return -1

=> 참고로 이방법은 LIS의 길이만 알 수 있고, 실제 LIS 구성 요소를 찾으려면 
추가적인 작업이 필요하다
2568번 문제 참고!
"""

# lower bound vs upper bound
# lower bound는 찾으려는값 '이상'의 값이 처음으로 나타나는 위치
# 따라서, key를 찾더라도 범위를 더 작은쪽으로 줄이는것 (arr[pc] == key일때 pr = pc 로 탐색)
# 반대로 upper bound는 찾으려는 값보다 '큰' 값이 처음으로 나타나는 위치
# 따라서 arr[pc] == key일때 upper bound는 pl = pc + 1이됨 그리고 탐색 이후에
# 실제 upper bound는 위에서 찾은 pl 값에서 1을 빼주어야 함! (pl = pc+1로 탐색하므로)
def lower_bound(arr, key):
    pl = 0
    pr = len(arr) - 1
    while pl < pr:
        pc = (pl + pr) // 2
        
        if arr[pc] >= key:
            pr = pc 
        else:
            pl = pc + 1

    return pl



N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

LIS = [numbers[0]]

# 포인트는 가장 긴 LIS를 만들기 위해서는 
# 마지막 요소가 최대한 낮은 값으로 유지되어야 한다는 것!
for i in range(1, N):
    now = numbers[i]
    # 현재 LIS 마지막 인덱스 값보다 큰 값이 오면 그냥 append
    if LIS[-1] < now:   
        LIS.append(now)
    # LIS 마지막 인덱스 값 이하의 값이 나오면 lower bound로 위치 찾아 LIS 요소와 교체
    else:
        idx = lower_bound(LIS, now)
        LIS[idx] = now

print(len(LIS))
