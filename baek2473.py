import sys
sys.stdin = open("baek2473.txt")

"""
전략 1.
하나는 그냥 최대한 0에 가까운 친구로
나머지는 투포인터로해서 가장 절댓값이 작아진 경우로
=> 반례는 -5 -1 2 3 4 이렇게 주어진 경우 -5, 2, 3을 골라야 한다.
포인트 1개를 순회한다면??
5000 * 5000 = 250만ㅇ이라서 가능!
이렇게범위에 따른 복잡도 추론이 가능해야한다.
"""


N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()


# point1 은 가장 절댓값 작은애로 체크 (어차피 최대 5000회다)
visited = [False] * N
min_sum = solutions[0] + solutions[1] + solutions[N-1]
pt1 = 1
pt2 = 0
pt3 = N-1
flag = False
# 위에 값이 0이 아닌경우만
if min_sum != 0:
    # 2부터 N-2까지 point1을 가정한다.
    for i in range(2, len(solutions)-1):
        if flag:
            break
        start = 0
        end = N-1
        min_tmp = solutions[start] + solutions[end] + solutions[i]
        # 절댓값이 작은애가 나올때마다 갱신
        if abs(min_tmp) < abs(min_sum):
            min_sum = min_tmp
            pt1 = i
            pt2 = 0
            pt3 = N-1
        while start < end:
            if start == i:
                start += 1
            if end == i:
                end -= 1
            # 혹시나 같아지면 break
            if start == end:
                break
            tmp = solutions[start] + solutions[end] + solutions[i]
            # 작은 절댓값이 나올때마다 갱신
            if abs(tmp) < abs(min_sum):
                min_sum = tmp
                pt1 = i
                pt2 = start
                pt3 = end
            if tmp < 0:
                start += 1
            elif tmp > 0:
                end -= 1
            # 0나오면 그냥 종료
            else:
                flag = True
                break
answer = [solutions[pt1], solutions[pt2], solutions[pt3]]
answer.sort()
print(" ".join(map(str, answer)))
