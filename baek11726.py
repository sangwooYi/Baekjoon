import sys
sys.stdin = open("baek11726.txt")

"""
DP는 크게
메모이제이션 개념과
최소 or 최대 개념을 이용해서 update하는 
두가지 방향으로 갈림! 
공통점은 점화식을 세울 수 있는 문제라는 것!
단순히 dfs돌리면 당근 시간초과
20만 넘어가도 오래걸린다.
메모이제이션 사용!
DP[n] = DP[n-1] + DP[n-2] 이거다!
(n길이의 사각형을 만드는 갯수는
n-1번쨰 길이에서 1짜리 추가 case + n-2번쨰 길이에서 2짜리 추가)
"""

def dfs(n):
    if n <= 2:
        return DP[n]
    for i in range(3, n+1):
        DP.append(DP[i-1] + DP[i-2])
    return (DP[n] % 10007)

N = int(input())
# DP[i] 는  2 *(i) 번쨰 사각형을 만드는 갯수
DP = [0, 1, 2]
ans = dfs(N)
print(ans)