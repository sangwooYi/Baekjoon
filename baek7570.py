import sys
sys.stdin = open("baek7570.txt")

"""
아이디어1.
최장 증가 부분수열 (LIS)를 찾아서 전체 길이에서 빼주는것???
하긴 100만 * 100만이니까 시간초과 되겠네
LIS 응용문제랍니다..
포인트가, 무작정 증가가 아니고, "연속되게 증가"하는 수열의 최장길이를 찾아야함
=> 얘는 이중for문이 아니고, 그냥 DP[idx] = DP[idx-1] + 1 인것,
(여기서 DP[a] 는 a 가 갖는 최대 연속 증가 수열 길이)
"""

N = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))


# 단순 LIS / LDS와는 좀 다르나, 결국 원리는 유사함! 
# 이 문제에서는 증가수열이 연속된 경우에만을 찾아야하므로 DP[idx] = DP[idx-1]+1이 된것!
DP = [0] * (N+1)
long = 0

for i in range(0, N):
    idx = order[i]
    # i-1번째 숫자가 i번쨰숫자보다 먼저 등장해야 한다. 이부분이 포인트!
    # i-1번째 숫자가 먼저 등장한 경우에는 숫자가 쌓이고, 안그러면 그냥 1임 (연속이 아닌 것)
    DP[idx] = DP[idx-1] + 1
    # DP[idx] 와 현재까지의 최장수열중 더 긴 값으로 갱신
    long = max(DP[idx], long) 

answer = N-long
print(answer)