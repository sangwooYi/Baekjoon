import sys
sys.stdin = open("baek14500.txt")

"""
이런 빡구현 문제도 익숙해져야 한다.
테트로미노 단위별 정사각형 만드는 기준을 잡자


위 모든 경우를 브루트포스로 돌려서 최대의 값을 찾자
M, N 의 최대가 500이므로 충분히 가능
( N, M >= 4) 따라서 아래 작업이 항상 가능
ㅡ, ㅣ 각각 슬라이딩 윈도우
ㅁ 슬라이딩 윈도우
나머지는 3x3 정사각형을 단위로해서 그 안에서 8가지씩이나온다, 그 3x3 정사각형을 단위로
슬라이딩 윈도우! 
"""

def find_max(a, b):
    if a > b:
        return a
    return b

def find_max_sum(arr, n, m):
    max_num = 0
    # ㅡ 모양
    for row in range(0, n):
        for col in range(0, m-3):
            temp_sum = 0
            for i in range(0, 4):
                temp_sum += arr[row][col+i]
            max_num = find_max(max_num, temp_sum)

    # ㅣ 모양
    for col in range(0, m):
        for row in range(0, n-3):
            temp_sum = 0
            for i in range(0, 4):
                temp_sum += arr[row+i][col]
            max_num = find_max(max_num, temp_sum)

    # ㅁ  모양
    for row in range(0, n-1):
        for col in range(0, m-1):
            temp_sum = 0
            for i in range(0, 2):
                for j in range(0, 2):
                    temp_sum += arr[row+i][col+j]
            max_num = find_max(max_num, temp_sum)
    
    # ㄱ 모양, ㅗ모양, ㄱㄴ모양 같이 체크  3 * 2 얘도 가로/세로 바꿔서
    for row in range(0, n-1):
        for col in range(0, m-2):
            # ㅡㄱ모양
            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row][col+i]
            temp_sum += arr[row+1][col+2]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row][col+i]
            temp_sum += arr[row+1][col]
            max_num = find_max(max_num, temp_sum)

            # ㄴㅡ 모양
            temp_sum = 0
            temp_sum += arr[row][col]
            for i in range(0, 3):
                temp_sum += arr[row+1][col+i]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            temp_sum += arr[row][col+2]
            for i in range(0, 3):
                temp_sum += arr[row+1][col+i]
            max_num = find_max(max_num, temp_sum)

            # ㅜ 모양
            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row][col+i]
            temp_sum += arr[row+1][col+1]
            max_num = find_max(max_num, temp_sum)
            # ㅗ 모양
            temp_sum = 0
            temp_sum += arr[row][col+1]
            for i in range(0, 3):
                temp_sum += arr[row+1][col+i]
            max_num = find_max(max_num, temp_sum)
        
            # ㄱㄴ 관련
            temp_sum = 0
            for i in range(0, 2):
                temp_sum += arr[row][col+i]
            for i in range(0, 2):
                temp_sum += arr[row+1][col+i+1]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            for i in range(0, 2):
                temp_sum += arr[row][col+i+1]
            for i in range(0, 2):
                temp_sum += arr[row+1][col+i]
            max_num = find_max(max_num, temp_sum)

    for col in range(0, m-1):
        for row in range(0, n-2):
            # ㄴ 모양
            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row+i][col]
            temp_sum += arr[row+2][col+1]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row+i][col]
            temp_sum += arr[row][col+1]
            max_num = find_max(max_num, temp_sum)

            # ㄱ 모양
            temp_sum = 0
            temp_sum += arr[row][col]
            for i in range(0, 3):
                temp_sum += arr[row+i][col+1]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            temp_sum += arr[row+2][col]
            for i in range(0, 3):
                temp_sum += arr[row+i][col+1]
            max_num = find_max(max_num, temp_sum)

            # ㅏ 모양
            temp_sum = 0
            for i in range(0, 3):
                temp_sum += arr[row+i][col]
            temp_sum += arr[row+1][col+1]
            max_num = find_max(max_num, temp_sum)
            # ㅓ 모양
            temp_sum = 0
            temp_sum += arr[row+1][col]
            for i in range(0, 3):
                temp_sum += arr[row+i][col+1]
            max_num = find_max(max_num, temp_sum)

            # ㄱㄴ 관련
            temp_sum = 0
            for i in range(0, 2):
                temp_sum += arr[row+i][col]
            for i in range(0, 2):
                temp_sum += arr[row+i+1][col+1]
            max_num = find_max(max_num, temp_sum)

            temp_sum = 0
            for i in range(0, 2):
                temp_sum += arr[row+i+1][col]
            for i in range(0, 2):
                temp_sum += arr[row+i][col+1]
            max_num = find_max(max_num, temp_sum)
    
    return max_num

N, M = map(int, input().split())
MAP = []
for i in range(0, N):
    temp = list(map(int, input().split()))
    MAP.append(temp)

answer = find_max_sum(MAP, N, M)
print(answer)