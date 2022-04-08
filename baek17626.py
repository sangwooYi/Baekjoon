import sys
sys.stdin = open("baek17626.txt")
"""
그리디 응용?

남은 숫자기준으로 루트 후 버림한 값이 출발점!
그때부터 1이될떄까지 for문돌리면서 BFS 계속 진행
먼저 도착한애가 승리! (DP에 저장하며 중복값 제거  )

DP를 어케써야되냐 ㅡㅡ?

DP 진짜 너무 어렵다 ..
DP[n] = min(DP[n-j**2], ....) + 1
# n을만들기위해서 DP[n-j**2] 에서 j**2을 더해서 만드는 모든 경우를 찾아 그 중 최솟값을 계속 업데이트!

"""


N = int(input())
# DP[n] 은 n을 만들기위한 최소의 갯수
DP = [0] * (N+1)
DP[0] = 0
DP[1] = 1

# 2부터 N까지 탐색
# 얘는 메모이제이션 개념?
for i in range(2, N+1):
    min_value = 9987654321   
    j = 1
    # j <= i**(1/2) 일떄까지 탐색 DP[0] 도 사용한다! DP[9] = DP[0] + 1 일테니까!!
    upper = i ** (1/2)
    while j <= upper:
        temp = min(min_value, DP[i-(j**2)])
        min_value = temp
        j += 1
    DP[i] = min_value + 1
print(DP[N])