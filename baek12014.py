import sys
sys.stdin = open("baek12014.txt")


# LIS 배열에 들어올 수 있는 가장 낮은 인덱스 위치를 찾는다.
def binary_search_left(arr, lis_arr, key):

    pl = 0
    pr = len(lis_arr)

    while pl < pr:
        pc = (pl+pr)//2
        # 조건에 만족하는 값이 나와도 범위를 줄인다.
        if lis_arr[pc] >= key:
            pr = pc
        else:
            pl = pc+1
    return pl




T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    prices = list(map(int, sys.stdin.readline().split()))

    LIS = [prices[0]]
    
    for i in range(1, N):
        price = prices[i]
        if LIS[-1] < price:
            LIS.append(price)
        else:
            idx = binary_search_left(prices, LIS, price)
            LIS[idx] = price
    print(f"Case #{tc}")
    if len(LIS) >= K:
        print(1)
    else:
        print(0)
        