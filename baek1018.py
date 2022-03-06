"""
chess: 문제명을 입력해주세요 :)
B
인덱스 짝수 행은 열이 짝수일때는 같은수여야하고 홀수면 다른수여야한다.
홀수 행은 반대로 짝수일때는 다른수 홀수있대는 같은수

그래서 시작을 B로 할떄 ,W로 할때 둘다 따지고
모든 경우 완전탐색해서 최솟값 찾는 문제
"""

import sys
sys.stdin = open('chess.txt')


def count_min(arr, n, m):
    min_count = 987654321

    for row in range(0, n-7):
        for col in range(0, m-7):
            count = 0
            count_inverse = 0
            start = arr[row][col]
            # 짝수 행 (인덱스 기준으로)
            for i in range(0, 8, 2):
                for j in range(0, 8):
                    # 나랑 같은애가 와야되는데
                    if j % 2 == 0:
                        # 나랑 다른애가 왔으면 그떄 count
                        if arr[row + i][col + j] != start:
                            count += 1
                        else:
                            count_inverse +=1
                    # 나랑 다른애가 와야 되는자리 
                    else:
                        # 나랑 같은애가 와있으면 count
                        if arr[row + i][col + j] == start:
                            count += 1
                        else:
                            count_inverse +=1
            # 홀수 행 (인덱스 기준으로)
            for i in range(1, 8, 2):
                for j in range(0, 8):
                    # 다른애가 와야 되는자리 근데 같은애가 와있으면 count
                    if j % 2 == 0:
                        if arr[row + i][col + j] == start:
                            count += 1
                        else:
                            count_inverse +=1
                    # 같은애가 와야디는데 다른애가 와있으면 count
                    else:
                        if arr[row + i][col + j] != start:
                            count += 1
                        else:
                            count_inverse +=1      
            # 돌떄마다 정산                      
            if min_count >= count:
                min_count = count
            if min_count >= count_inverse:
                min_count = count_inverse
    # 최솟값이 저장 되어 있다.
    return min_count

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(0, N)]
answer = count_min(MAP, N, M)
print(answer)