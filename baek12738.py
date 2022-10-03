import sys
sys.stdin = open("baek12738.txt")


"""
단순히 길이만 구하는 것은,

LIS[-1] < arr[i] 라면 
그냥 LIS에 추가,
아니라면,
lower bound를 통해, 적절한 위치를 탐색 후
LIS[pl] < arr[i] 면 LIS[-1] = arr[i]
아니라면 LIS[pl] = num

길이만 구할거면 위에서 끝,
만약 실제 요소까지 구해야 하면,
매 요소마다 해당 LIS 위치 인덱스를 DP[i]에 저장
(LIS에서 이 요소의 위치를 미리 저장해 두는것)
ex) LIS[-1] < arr[i] 라면 DP[i] = len(LIS)-1 (append 후 위치, 즉 현재 LIS위치의 맨 끝 인덱스)

참고, bisection_left를 쓰거나 그냥 구현

그냥 이분탐색
while pl <= pr:
    pc = (pl+pr)//2
    if arr[pc] == key:
        탐색 완료
        break
    elif arr[pc] > key:
        pr = pc-1
    else:
        pl = pc+1

lower bound 는 가장 처음 해당 조건을 만족하는 순간을 찾는 것
즉 arr[pc] = key를 찾았더라도 pr = pc / for finding lower bound
while pl < pr:
    pc = (pl+pr)//2
    if arr[pc] >= key:
        pr = pc
    else:
        pl = pc+1
위 탐색 결과 이후 pl 값이 lower bound

upper bound 는 해당 조건을 만족하다가 만족하지 않는 첫 순간을 탐색, 즉 해당 조건의 마지막 끝을 찾음
즉 arr[pc] = key를 찾았더라도 pl = pc+1 / for finding upper bound
while pl < pr:
    pc = (pl+pr)//2
    if arr[pc] > key:
        pr = pc
    else:
        pl = pc+1
위 탐색 결과 이후 pl-1 값이 upper bound (pl = pc+1 로 하기때문에, 탐색 후 pl은 영역을 하나 벗어난다.)
"""


# 얘는 길이만!
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

LIS = [nums[0]]
for i in range(1, N):
    num = nums[i]
    if LIS[-1] < num:
        LIS.append(num)
    else:
        pl = 0
        pr = len(LIS)-1
        
        # lower bound
        while pl < pr:
            pc = (pl+pr)//2
            if LIS[pc] >= num:
                pr = pc
            else:
                pl = pc+1
        LIS[pl] = num
print(len(LIS))