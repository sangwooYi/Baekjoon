import sys
sys.stdin = open("baek1461.txt")

"""
아이디어1.
책의 갯수가 50미만이다.
따라서 음수 / 양수 구분한뒤 절댓값 기준 내림차순
그다음 M 개씩 끊는다.
=> 각 집합에서 가장 큰 값의 절댓값 만큼 이동
책의 갯수가 0이면 종료
아니면 원점으로 이동

=> 이 과정에서의 총 이동 거리가 최종 답.

"""

def calc_min_path(books, n, m):
    pos_position = []
    neg_position = []
    
    # 이동 정보에 대해 저장
    moving_arr = []
    res = n
    # 이동거리
    move = 0
    for i in range(0, n):
        temp = books[i]
        # 양수
        if temp > 0:
            pos_position.append(temp)
        # 음수
        else:
            neg_position.append(temp)
    # 양수의 경우 내림차순
    pos_position.sort(key=lambda x : -x)
    # 음수의 경우는 오름차순 (절댓값으로는 내림차순)
    neg_position.sort()

    # 있는 경우만
    if pos_position:
        idx = 0
        while idx < len(pos_position):
            path = pos_position[idx]
            moving_arr.append(path)
            idx += m

    # 있는 경움만
    if neg_position:
        idx = 0
        while idx < len(neg_position):
            path = -neg_position[idx]
            moving_arr.append(path)
            idx += m
    # 크기순 정렬, 가장 큰 값만 1번 (이때 종료) 나머지는 왕복 
    moving_arr.sort()
    for i in range(0, len(moving_arr)):
        if i == len(moving_arr) - 1:
            move += moving_arr[i]
        else:
            move += (2*moving_arr[i])
    return move

# 책의 갯수, 한번에 들 수 있는 갯수
N, M = map(int, input().split())
# 책 위치
BOOK = list(map(int, input().split()))

answer =  calc_min_path(BOOK, N, M)
print(answer)