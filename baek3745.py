import sys
sys.stdin = open("baek3745.txt")


"""
LIS 
nO(logn) 으로 푸는 문제!

길이만 체크하는 것은
=> LIS 배열의 가장 마지막 값보다 다음오는 값이 크면 => 그냥 추가
=> 아니라면 이분탐색을 통해, 해당 값이 들어올 수 있는 가장 작은 위치를 탐색, 그 위치에 값을 넣어준다

=> 최종 LIS 길이가 LIS 길이
실제 값까지 출력해야 한다면 DP 배열을 통해
현재 인덱스 값이 LIS 배열 몇번 인덱스에 들어갔는지를 체크
ex ) LIS에서 2번째 위치에 온 값이라면 DP[i] = 1 (인덱스는 0부터) 이런식
그리고 DP 배열을 역순으로 순회하며 r-1 ~ 0 까지 현재의 LIS 위치값을 갖는
숫자를 찾음 (동일한 위치값이 여러개라도 그냥 가장 먼저 탐색된 애를 추가해주면 됨)

그다음 sort하면 우리가 원하는 정답
(그래서 애초에 답이 여러개 나올 수 있다.)
"""

def binary_search_left(key, pl, pr):

    while pl < pr:
        
        pc = (pl+pr)//2
        # 다음 탐색값을 더 줄이는 경우
        # lower bound 이므로, 원하는 조건이 나와도 다음 탐색값을 줄인다.
        if LIS[pc] >= key:
            pr = pc
        # 다음 탐색값을 늘리는 경우
        else:
            pl = pc+1
    return pl

while True:
    # 종료조건이 따로 없을때 종료하는 방법!
    N = sys.stdin.readline()
    if not N:
        break
    N = int(N)
    nums = list(map(int, sys.stdin.readline().split()))

    LIS = [nums[0]]
    for i in range(1, N):
        num = nums[i]

        if LIS[-1] < num:
            LIS.append(num)
        else:
            idx = binary_search_left(num, 0, len(LIS))
            LIS[idx] = num
    print(len(LIS))