import sys
sys.stdin = open("baek14890.txt")

"""
경사로는 높이가1이며, 최대 L만큼 공간이 필요

놓을 수 없는 경우는
1. 높이차이 1 초과
2. 이미 놓여진 경사로에 또 경사로를 놓거나 겹치는 경우
3. 낮은 곳의 높이가 균일하지 않은경우 (즉 L개의 연속된 같은 높이가 필요한것)
4. 범위를 벗어나는 경우

위 범위에서 안걸리면 가능한 경사로인것

걍 완전 구현문제
"""

def count_possible(arr, n, l):
    count = 0
    # 행검사
    for row in range(0, n):
        # 매번 체크 ,경사로 중복 여부 체크
        visited = [False] * n
        flag = True
        col = 0
        while col < n-1:
            now_h = arr[row][col]
            next_h = arr[row][col+1]
            # 높이차이가 1 초과, 더이상 볼 필요 X
            if abs(now_h - next_h) > 1:
                flag = False
                break
            # 오히려 오르막길인 경우, 역으로 추적해야함
            if next_h > now_h:
                # 역으로 l만큼 길이가 필요, 근데 전부 높이가 같아야 함
                # 범위 밖
                if col-(l-1) < 0:
                    flag = False
                    break
                for k in range(0, l):
                    # 이미 경사로가 존재
                    if visited[col-k]:
                        flag = False
                        break
                    # 높이가 다름
                    if arr[row][col-k] != now_h:
                        flag = False
                        break
                if not flag:
                    break
                # 경사로 놓을 수 있으면 visited 처리
                for k in range(0, l):
                    visited[col-k] = True
                col += 1
            # 내리막길인 경우
            elif now_h > next_h:
                # 맵 밖인 경우
                if col + l >= n:
                    flag = False
                    break
                # l만큼 길이가 필요, 근데 전부 높이가 같아야 함
                for k in range(1, l+1):
                    # 높이가 다름
                    if arr[row][col+k] != next_h:
                        flag = False
                        break
                if not flag:
                    break
                # 경사로 놓을 수 있으면 visited 처리
                for k in range(1, l+1):
                    visited[col+k] = True
                col += l
            # 모든 경우는 다음칸으로 이동
            else:
                col += 1
        # 가능한 길
        if flag:
            count += 1

    # 열검사
    for col in range(0, n):
        visited = [False] * n
        flag = True
        row = 0
        while row < n-1:
            now_h = arr[row][col]
            next_h = arr[row+1][col]
            # 높이차이가 1 초과, 더이상 볼 필요 X
            if abs(now_h - next_h) > 1:
                flag = False
                break
            # 오히려 오르막길인 경우, 역으로 추적해야함
            if next_h > now_h:
                # 역으로 l만큼 길이가 필요, 근데 전부 높이가 같아야 함
                # 범위 밖
                if row-(l-1) < 0:
                    flag = False
                    break
                for k in range(0, l):
                    # 이미 경사로가 존재
                    if visited[row-k]:
                        flag = False
                        break
                    # 높이가 다름
                    if arr[row-k][col] != now_h:
                        flag = False
                        break
                if not flag:
                    break
                # 경사로 놓을 수 있으면 visited 처리
                for k in range(0, l):
                    visited[row-k] = True
                row += 1
            # 내리막길인 경우
            elif now_h > next_h:
                # 맵 밖인 경우
                if row + l >= n:
                    flag = False
                    break
                # l만큼 길이가 필요, 근데 전부 높이가 같아야 함
                for k in range(1, l+1):
                    # 높이가 다름
                    if arr[row+k][col] != next_h:
                        flag = False
                        break
                if not flag:
                    break
                # 경사로 놓을 수 있으면 visited 처리
                for k in range(1, l+1):
                    visited[row+k] = True
                row += l
            # 모든 경우는 다음칸으로 이동
            else:
                row += 1
        # 가능한 길
        if flag:
            count += 1

    return count

N, L = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

answer = count_possible(MAP, N, L)
print(answer)