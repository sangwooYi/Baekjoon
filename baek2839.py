import sys
sys.stdin = open("baek2839.txt")

"""
그리드 응용!
1. 우선 5의 배수로 최대한 체크
2. 나머지 없으면 끝. 있으면 남은 수가 3의 배수인지 체크
3. 3의배수이면 그냥 진행 go
4. 아니라면 될때까지 +5 씩 되돌아감
5. 3의배수가 되면 그제서야 진행 최종 값 반환
5. 끝까지 3의배수 안되면 -1 반환
"""


def find_min_bag(n):
    num_small = 0
    num_large = 0

    num_large = n // 5
    res = n % 5
    # 5로 나누어 떨어지면 끝
    if res == 0:
        return num_large
    # 5로나눈 나머지가 3으로 나누어떨어지면 끝
    if res % 3 == 0:
        num_small = res // 3
        return num_large + num_small
    while num_large > 0:
        num_large -= 1
        res += 5
        # 3의배수 될떄까지 5씩 더함
        if res % 3 == 0:
            num_small = res // 3
            return num_large + num_small
    # 여기까지 왔다는건 그냥 5의 배수도 3의배수도 아닌것
    return -1


N = int(input())
answer = find_min_bag(N)
print(answer)