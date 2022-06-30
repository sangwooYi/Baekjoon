import sys
sys.stdin = open("baek2565.txt")

"""
전선이 교차하는 조건

A1 < A2 라면 B1 > B2 
A1 > A2 라면 B1 < B2
즉 (A1-A2) * (B1-B2) < 0 이되야 하는것

근데 여기서 문제는 LIS 구하는 문제 (최장 증가수열)
줄세우기랑 유사한 문제라고 생각하면 될듯

A기준 오름차순 정렬후 B 기준, LIS 를 구하면 N-(그 숫자) = 답이된다.
why? => 결국 위 교차조건인것
A 기준 오름차순으로 보면서 그 때 B도 역시 증가한다면 
(A1-A2) * (B1-B2) > 0 이란소리니까! 이것의 최대 길이를 구한것이므로, 무조건 
N-LIS 가 답인것! (이런 로직을 혼자 생각ㄷㄷ)
전깃줄2 무조건 풀어볼것! 
"""


N = int(input())
arr = [0] * N

for i in range(0, N):
    a, b = map(int, input().split())
    arr[i] = [a, b]

arr.sort()

DP = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            DP[i] = max(DP[i], DP[j]+1)

answer = N - (max(DP))
print(answer)