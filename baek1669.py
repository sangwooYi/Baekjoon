import sys
sys.stdin = open("baek1669.txt")


X, Y = map(int, input().split())
diff = Y-X


answer = 0
n = 0

# 차이가 없으면 그냥 바로 끝
if diff > 0:
    
    while n**2 < diff:
        n += 1

    # 정확히 같은 값이 아니면 1 빼준다
    if n**2 != diff:
        n -= 1

    answer = 2*n-1

    # n**2 을 빼고 나머지 값에 대해서 계산해야함
    diff -= n**2

    while diff > 0:
        # 이부분 중요
        diff -= min(n, diff)
        answer += 1
    
print(answer)