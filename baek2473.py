import sys
sys.stdin = open("baek2473.txt")


N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()


# point1 은 가장 절댓값 작은애로 체크 (어차피 최대 5000회다)
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
