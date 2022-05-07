"""
경우의 수는 곱하기다! 주의!
진짜 이런건 제발 혼자서 풀자 ㅠㅠ
"""

N = int(input())
if N % 2:
    answer = 0
else:
    DP = [0] * (N+1)
    DP[2] = 3
    # 사실상 4부터
    if N > 2:
        for i in range(4, N+1, 2):
            # i-2는 3가지씩
            DP[i] = (DP[i-2] * 3)
            point = i-4
            # 경우의수가 2가지씩 계속 나옴
            while point > 0:
                DP[i] += DP[point] * 2
                point -= 2
            DP[i] += 2
    answer = DP[N]
print(answer)