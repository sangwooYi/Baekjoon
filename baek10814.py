import sys
sys.stdin = open("baek10814.txt")
"""
아래 구문 꼭 외워두자
.sort(key=lambda x: (정렬 기준 순서대로))
# 아래같이 하면 0번 인덱스 기준 정렬하고 같은 값끼리는 1번 인덱스 기준으로 또 정렬
.sort(key=lambda x: (x[0], x[1])
"""


N = int(sys.stdin.readline())
MAP = [0] * N   
for i in range(0, N):
    temp = list(sys.stdin.readline().split())
    # 부분만 바꾸려면 그냥 이렇게
    temp[0] = int(temp[0])
    temp.append(i)
    MAP[i] = temp
# 일단 나이순으로 오름차순, 같은 나이끼리는 입력순으로 역시 오름차순
MAP.sort(key=lambda x: (x[0], x[2]))
for i in range(0, N):
    # 세번째 인덱스는 임시용 출력할 필요 X
    for j in range(0, 2):
        if j == 1:
            print(MAP[i][j])
        else:
            print(MAP[i][j], end=" ")