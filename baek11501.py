import sys
sys.stdin = open("baek11501.txt")


T = int(sys.stdin.readline())
for i in range(0, T):
    N = int(sys.stdin.readline())
    stocks = list(map(int, sys.stdin.readline().split()))

    answer = 0
    # 가능한 최대가격일때 몽땅 팔아야함 (거꾸로 탐색하면 훨씬 편함)
    max_price = 0
    for i in range(N-1, -1, -1):
        max_price = max(max_price, stocks[i])

        answer += (max_price-stocks[i])
    print(answer)
