import sys
sys.stdin = open("baek11660.txt")
"""
아래처럼 해도 시간초과네 ㅡㅡ?
이거 어떻게하면 시간 줄일지 고민좀 해보자
"""

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))
# idea 이미 한번 순회한 값은 저장해서 또나오면 사용한다. 
dynamic_dict = {}

for i in range(0, M):
    # 튜플은 key로 사용 가능
    # 주어지는 좌표값과 인덱스가 1씩차이난다 조심!
    coords = tuple(map(int, sys.stdin.readline().split()))
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    if coords in dynamic_dict.keys():
        print(dynamic_dict[coords])
    else:
        sum = 0
        # x1 ~ x2까지 순회하려면 (x1-1 ~ x2-1 가지 순회하는거!) 항상 인덱스-값 연동할때는 조심
        for row in range(x1-1, x2):
            for col in range(y1-1, y2):
                sum += MAP[row][col]
        dynamic_dict[coords] = sum
        print(sum)