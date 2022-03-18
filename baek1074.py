import sys
sys.stdin = open("baek1074.txt")

"""
분할정복!
0 1   0 -> 1 -> 2 -> 3 순서로 재귀를 계속 진행
2 3   row/col 의길이가 2가 될때까지 계속 재귀 진행 
그리고 길이가 1이라면 그냥 전역 변수 order 값을 1증가해주고 return (종료조건)
그리고 그 값이 문제에서 찾으려는 r행 c열인지 확인해서 맞으면 global answer값에 저장 
2**N 에서 N의 최댓값이 15 따라서, 재귀 중첩횟수도 (깊이) 최대 15 (할만함)

pl, pr, pu, pd 이렇게 네가지변수를 전달하고 pl == pr (col)&& pu == pd (row)일때가 종료조건이되도록!

방법은 맞는데 N이 12만되도 3초가 넘게 걸린다.

효율화 필요!
찾으려는 row, col이 없는 범위를 굳이 체크할 필요가 없다!
그리고 현재 분할된 박스 길이가 2**N 일때,
각 영역의 시작점은
기준점 + ((2**(N-1))**2)*0  
기준점 + ((2**(N-1))**2)*1
기준점 + ((2**(N-1))**2)*2
기준점 + ((2**(N-1))**2)*3
이라는 규칙을 갖고있다 이부분을 같이 활용하면 효율화 가능

따라서 매 반복마다 4영역중에 어디 영역에 속하는지 체크
-> N이 0이 될때까지 감소
N이 0이면 현재 기준점을 출력하면 끝
"""


# 요건 가장 무식하게 재귀 돌린 경우, 쓸데없는 재귀가 너무많아서 효율성이 떨어짐
# def find_order(pl, pr, pu, pd, r, c):
#     global order
#     global answer
#     # 계속 동시에 쪼개므로 굳이 pu==pd 까지 따질 필요도 없다.
#     # 길이가 1이 된 경우 (종료 조건)
#     if pl == pr:
#         row = pu
#         col = pl
#         order += 1
#         if row == r and col == c:
#             answer = order
#         return
#     # 세로
#     r_mid = (pu + pd) // 2
#     # 가로
#     c_mid = (pl + pr) // 2
#     # 좌상
#     find_order(pl, c_mid, pu, r_mid, r, c)
#     # 우상
#     find_order(c_mid+1, pr, pu, r_mid, r, c)
#     # 좌하
#     find_order(pl, c_mid, r_mid+1, pd, r, c)
#     # 우하
#     find_order(c_mid+1, pr, r_mid+1, pd, r, c)

def find_order(l, r, u, d, n, row, col, point):
    # 종료 조건
    global answer
    if n == 0:
        if u == row and l == col:
            answer = point
        return
    term = (2**(n-1))**2
    row_mid = (u + d) // 2
    col_mid = (l + r) // 2
    
    # 아래 중에서 조건에 해당되는 경우 재귀만 진행 (영역에 안들어오는 부분을 굳이 돌릴 필요가 X)
    # 좌상
    if row <= row_mid and col <= col_mid:
        next_point = point
        find_order(l, col_mid, u, row_mid, n-1, row, col, next_point)
    # 우상
    if row <= row_mid and col > col_mid:
        next_point = point + (term*1)
        find_order(col_mid+1, r, u, row_mid, n-1, row, col, next_point)
    # 좌하
    if row > row_mid and col <= col_mid:
        next_point = point + (term*2)
        find_order(l, col_mid, row_mid+1, d, n-1, row, col, next_point)
    # 우하
    if row > row_mid and col > col_mid:
        next_point = point + (term*3)
        find_order(col_mid+1, r, row_mid+1, d, n-1, row, col, next_point)


N, R, C = map(int, input().split())
# 첫번째순서가 0으로 출력되므로 -1 부터 시작
left = 0
right = (2**N) - 1
up = 0
down = (2**N) - 1
start = 0
answer = 0
find_order(left, right, up, down, N, R, C, start)
print(answer)