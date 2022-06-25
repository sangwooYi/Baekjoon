import sys
sys.stdin = open("baek2467.txt")

"""
전략1.

그냥 내가 떠오르는 풀이 방법으로 풀자.
투 포인터 알고리즘으로만도 풀 수 있는 문제
(Why? 최대 요소가 10만개니까)

처음 내 전략이 맞았다. .. 나를 믿자!

처음 시작은 
0, N-1

현재 용액합의 절댓값 / 저장된 절댓값 비교해서 작은 값으로 갱신

그 후

두 용액 합이 < 0 이면 start += 1 (더 큰값이 필요하므로)
             > 0 이면 end -= 1 (더 작은 값이 필요하므로)
             = 0 이면 끝 break (더 볼 필요도 없다.)
"""

N = int(input())
solutions = list(map(int, input().split()))

start = 0
end = N-1
min_sum = abs(solutions[start] + solutions[end])

answer = [solutions[start], solutions[end]]

while start < end:
    now = solutions[start] + solutions[end]
    tmp_sum = abs(now)

    # 현재 임시합이 더 작으면 갱신
    if tmp_sum < min_sum:
        answer = [solutions[start], solutions[end]]
        min_sum = tmp_sum
    
    if now < 0:
        start +=1
    elif now > 0:
        end -= 1
    # 0이면 그냥 종료
    else:
        break
print(" ".join(map(str, answer)))
