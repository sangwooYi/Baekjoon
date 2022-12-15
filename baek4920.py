import sys
sys.stdin = open("baek4920.txt")

"""
조심하자!
모든 경우가 다되는 것이아니라,
90도 회전일때 나올 수 있는경우만이다!
따라서 ㄱ 의 경우 반전까지 포함하면
총 8가지가 존재하나, 90도 회전으로만 나올 수 있는경우는 4가지!

ㄱㄴ 도 원래는 4가지이나 ,회전만으로는 2가지만 가능!
"""


def find_max(arr):

    n = len(arr)

    # 최댓값 저장 용
    # 전부 음수일 수도 있다. 조심하자!
    res = -987654321987

    # 1-1번 (일자형 ㅡ 형태)
    for row in range(0, n):
        for col in range(0, n-3):
            tmp = 0
            for k in range(0, 4):
                tmp += arr[row][col+k]
            res = max(res, tmp)
    # 1-2번 (일자형 ㅣ 형태)
    for col in range(0, n):
        for row in range(0, n-3):
            tmp = 0
            for k in range(0, 4):
                tmp += arr[row+k][col]
            res = max(res, tmp)
    # 2번 ㅁ 형태
    for row in range(0, n-1):
        for col in range(0, n-1):
            tmp = 0
            for i in range(0, 2):
                for j in range(0, 2):
                    tmp += arr[row+i][col+j]
            res = max(res, tmp)

    # 2*3 직사각형
    for row in range(0, n-1):
        for col in range(0, n-2):
            # 3-1-1 ㄱㄴ 모양
            tmp = 0
            for i in range(0, 2):
                for j in range(i, i+2):
                   tmp += arr[row+i][col+j]
            res = max(res, tmp) 

            # 4-1-1 ㅗ 모양
            tmp = 0
            for j in range(0, 3):
                tmp += arr[row+1][col+j]
            tmp += arr[row][col+1]
            res = max(res, tmp)
            
            # 4-1-2 ㅜ 모양    
            tmp = 0
            for j in range(0, 3):
                tmp += arr[row][col+j]
            tmp += arr[row+1][col+1]
            res = max(res, tmp)

            # 5-1-1 ㄱ모양
            tmp = 0
            for j in range(0, 3):
                tmp += arr[row][col+j]
            tmp += arr[row+1][col+2]
            res = max(res, tmp)

            # 5-1-2 ㄴ 모양
            tmp = 0
            for j in range(0, 3):
                tmp += arr[row+1][col+j]
            tmp += arr[row][col]
            res = max(res, tmp)


    # 3*2 직사각형
    for row in range(0, n-2):
        for col in range(0, n-1):
            # 3-2-2
            tmp = 0
            for j in range(0, 2):
                for i in range(1-j, 3-j):
                    tmp += arr[row+i][col+j]
            res = max(res, tmp)
    
            # 4-2-1 ㅏ 모양
            tmp = 0
            for i in range(0, 3):
                tmp += arr[row+i][col]
            tmp += arr[row+1][col+1]
            res = max(res, tmp)

            # 4-2-2 ㅓ 모양
            tmp = 0
            for i in range(0, 3):
                tmp += arr[row+i][col+1]
            tmp += arr[row+1][col]
            res = max(res, tmp)

            # 5-2-3번 ㄱ모양 좌우반전
            tmp = 0
            for i in range(0, 3):
                tmp += arr[row+i][col]
            tmp += arr[row][col+1]
            res = max(res, tmp)

            # 5-2-4번 ㄴ모양 좌우반전
            tmp = 0
            for i in range(0, 3):
                tmp += arr[row+i][col+1]
            tmp += arr[row+2][col]
            res = max(res, tmp)
    return res



tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    tc += 1
    MAP = [0] * N
    for i in range(0, N):
        MAP[i] = list(map(int, input().split()))

    answer = find_max(MAP)
    print(f"{tc}. {answer}")
