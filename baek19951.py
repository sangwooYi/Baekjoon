import sys
sys.stdin = open("baek19951.txt")

"""
누적합 배열을 이용해서 a~b 까지 일정한 변화를 여러번 시키는 문제 풀 때 사용!

ex) 
N이 6인 배열에서
1 ~ 3까지 +2 씩, 2~5씩 -4씩 해라는 작업을 할때
[2, -4, 0, -2, 0, 4] 이 형태의 배열의 누적합을 구한 후 
이와, 원 배열과 연산 시키는것!
=> 저 누적합 배열이 [2, -2, -2, -4, -4, 0] 이 되는식!
"""


N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

tmp_arr = [0] * N
for i in range(0, M):
    a, b, k = map(int, sys.stdin.readline().split())
    tmp_arr[a-1] += k
    if b < N:
        tmp_arr[b] -= k

sum_arr = [0] * N
sum_arr[0] = tmp_arr[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1]+tmp_arr[i]

answer = [0] * N
for i in range(0, N):
    answer[i] = H[i] + sum_arr[i]
print(" ".join(map(str, answer)))