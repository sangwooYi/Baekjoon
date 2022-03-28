import sys
sys.stdin = open("baek6064.txt")
"""
다음 해를 표기할 떄
<x:y> 다음해를 <x':y'> 로 표기할떄
x < M이면 x' = x+1 / x >= M 이면 x' = 1
y < N 이면 y' = y+1 / y >= N 이면 y'= 1

응용하면
만약 (x - a) == (y - b) 라면 같은 step만큼 이동해서 맞출 수 있는것
따라서 현재 count += step 만큼이 답이 됨
(m - a) , (n - b) 중 작은값만큼 점프 + 그만큼 count 추가

내 코드에 대해 확신이 없을 때
반례를 생각하는것도 실력이다!!
"""

def calendar(m, n, x, y):
    count = 1 
    a = 1
    b = 1
    if x == 1 and y == 1:
        return 1
    while True:
        # x == a and y == b 인경우도 체크해야지! ㅡㅡ
        if (x - a) == (y - b) and x >= a:
            step = x - a
            return count + step
        term = min(m-a, n-b)
        count += term
        a += term
        b += term
        if a == m and b == n:
            # 이게 답인 경우
            if x == m and y == n:
                return count
            break
        if a == m:
            a = 1
            b += 1
            count += 1
            continue
        if b == n:
            b = 1
            a += 1
            count += 1
            continue
    return -1

T = int(input())
for tc in range(1, T+1):
    M, N, X, Y = map(int, input().split())
    ans = calendar(M, N, X, Y)
    print(ans)