import sys
sys.stdin = open("baek1946.txt")

"""
문제 이해를 잘하자.
특정 합격자에 비해 하나라도 등수가 떨어지면 그 지원자는 못뽑힌다는 문제!
"""

T = int(sys.stdin.readline())

for tc in range(0, T):
    N = int(sys.stdin.readline())
    candidates = [0] * N
    for i in range(0, N):
        # 점수가 아니라 순위다!
        a, b = map(int, sys.stdin.readline().split())
        candidates[i] = [a, b]
    # 우선 하나를 기준으로 오름차순 정렬
    candidates.sort()

    # 일단 한분야에 1등을 뽑음
    tmp = candidates[0]
    cnt = 1
    for i in range(1, N):
        # 다음 지원자는 이미 정렬기준 순위는 밀리기 때문에,
        # 다른 분야는 현재 기준 지원자보다 순위가 높아야 뽑힐수 있다!
        if tmp[1] > candidates[i][1]:
            cnt += 1
            tmp = candidates[i]
    print(cnt)
