import sys
sys.stdin = open("baek17951.txt")

"""
이분탐색에서 핵심은
left / right를 어떻게 잡고
목표 값을 mid로 설정,
그리고 해당 목표값으로 작업이 가능한지
'가능 여부' 를 묻는 문제!

현재 mid 값을 최솟값으로 쪼갤 때 K개 이상이 나오면 => 더 줄일 수 있음
안되면 => 현재보다 큰 값이 필요 하다는 뜻!


여기서는 left는 0점 right는 받을 수 있는 최대 점수 N*20 이 되는것!

이분탐색 문제 많이 풀어보자!

이문제는 upper bound 문제! 

upper bound : 현재 조건이 가능한 가장 최댓값 
따라서, 현재 원하는 값이 나와도 , 더 큰 값을 탐색 
=> 탐색 이후 left에는 현재 조건이 불가능한 가장 처음 값이 담겨있다 (따라서 답은 left-1)

while pl < pr:
    pc = (pl+pr)//2

    # 더 값을 키울 필요가 있음 (원하는 값이 나와도 다음 탐색값을 키운다.)
    if pc <= key:
        pl = pc+1
    # 더 값을 줄일 필요가 있음
    else:
        pr = pc


lower bound : 현재 조건이 가능한 가장 처음 값 
따라서, 현재 원하는 값이 나와도 더 작은 값을 탐색
=> 탐색 이후 나온 left값이 답이 됨

while pl < pr:
    pc = (pl+pr) // 2

    # 값을 키울 필요가 있음
    if pc < key:
        pl = pc+1
    # 값을 줄일 필요가 있음 (원하는 값이 나와도 다음 탐색값을 줄인다.)
    else:
        pr = pc


일반적인 binary search => 그냥 값이 나오는지만 확인

while pl <= pr:
    pc = (pl+pr) // 2

    # 그냥 값이 나오면 종료
    if pc == key:
        answer = pc
    elif pc < key:
        pl = pc+1
    
    else:
        pr = pc-1
        
"""


N, K = map(int, sys.stdin.readline().split())
sheets = list(map(int, sys.stdin.readline().split()))


left = 0
# lower bound / upper bound 문제 풀 때는 최대 범위 + 1 을 right로 잡아주어야 함!
right = N*20+1


# 그냥 upper bound 이다
# upper bound / lower bound 일때는 left < right가 조건으로 들어감. 일반적 binary Search 랑 살짝 다름!
while left < right:
    mid = (left + right)//2

    score = 0
    group = 0

    for sheet in sheets:
        score += sheet
        
        if score >= mid:
            group += 1
            score = 0
    # 현재 값은 K그룹으로 나누기에는 너무 큼. (따라서 찾으려는 값보다 큰 상태)
    if group < K:
        right = mid
    # 현재 값은 K그룹으로 나누기에 충분, 따라서 더 큰 값을 적용해 보아도 된다.
    else:
        left = mid+1
print(left-1)

