import sys
sys.stdin = open("baek12100.txt")
sys.setrecursionlimit(10**5)


"""
얘는 DFS, BFS 둘다 가능할듯?

종료조건은
1. 5회 끝난 경우,
2. 5회 이내라도 더이상 움직일 블록이 없는 경우
조심하건 한번 합쳐진건 더이상 못합쳐진다. (이부분 예외처리가 안됨)

빡구현 미쳤네 ㅡㅡ
"""
# 깊이, MAP, 방향, N(사이즈)
def dfs(depth, arr, d, n):
    global answer
    temp = [[0] * n for _ in range(0, n)]
    # 해당위치에서 병합이 된적 있는지 체크
    visited = [[False] * n for _ in range(0, n)]
    # 방향에 따라서 순회방향을 다르게 하는게 유리
    # 위
    # 이동이 없는지 체크해야 함
    flag = False
    if d == 0:
        for row in range(0, n):
            for col in range(0, n):
                # 값이 있는애만 체크
                if arr[row][col]:
                    # 첫줄은 그냥 그대로
                    if row == 0:
                        temp[row][col] = arr[row][col]
                    else:
                        k = 1
                        while (row-k) >= 0:
                            # 해당 위치가 0이면 계속이동
                            if temp[row-k][col] == 0:
                                # 끝까지 0만있는경우
                                flag = True
                                if (row-k) == 0:
                                    temp[row-k][col] = arr[row][col]
                                    break
                                k += 1
                            # 블록을 만난경우, 처리하고 종료
                            else:
                                # 같으면 합쳐짐
                                if temp[row-k][col] == arr[row][col]:
                                    if not visited[row-k][col]:
                                        flag = True
                                        # 병합처리
                                        visited[row-k][col] = True
                                        temp[row-k][col] += arr[row][col]
                                    else:
                                        # 이미 병합된 장소면 병합 불가
                                        if k > 1:
                                            flag = True
                                        temp[row-k+1][col] = arr[row][col]

                                else:
                                    # 다른값이면 그냥 그 전위치에
                                    if k > 1:
                                        flag = True
                                    temp[row-k+1][col] = arr[row][col]
                                break
    # 아래  
    elif d == 1:
        for row in range(n-1, -1, -1):
            for col in range(0, n):
                if arr[row][col]:
                    # 마지막줄은 그대로
                    if row == n-1:
                        temp[row][col] = arr[row][col]
                    else:
                        k = 1
                        while (row+k) < n:
                            if temp[row+k][col] == 0:
                                flag = True
                                if (row+k) == n-1:
                                    temp[row+k][col] = arr[row][col]
                                    break
                                k += 1
                            else:
                                if temp[row+k][col] == arr[row][col]:
                                    if not visited[row+k][col]:
                                        flag =  True
                                        visited[row+k][col] = True
                                        temp[row+k][col] += arr[row][col]
                                    else:
                                        if k > 1:
                                            flag = True
                                        temp[row+k-1][col] = arr[row][col]  
                                else:
                                    if k > 1:
                                        flag = True
                                    temp[row+k-1][col] = arr[row][col]
                                break
    # 좌
    elif d == 2:
        for col in range(0, n):
            for row in range(0, n):
                if arr[row][col]:
                    if col == 0:
                        temp[row][col] = arr[row][col]
                    else:
                        k = 1
                        while (col-k) >= 0:
                            if temp[row][col-k] == 0:
                                flag = True
                                if (col-k) == 0:
                                    temp[row][col-k] = arr[row][col]
                                    break
                                k += 1
                            else:
                                if temp[row][col-k] == arr[row][col]:
                                    if not visited[row][col-k]:
                                        flag = True
                                        visited[row][col-k] = True
                                        temp[row][col-k] += arr[row][col]
                                    else:
                                        if k > 1:
                                            flag = True
                                        temp[row][col-k+1] = arr[row][col]
                                else:
                                    if k > 1:
                                        flag = True
                                    temp[row][col-k+1] = arr[row][col]
                                break 
                                    
    # 우
    elif d == 3:
        for col in range(n-1, -1, -1):
            for row in range(0, n):
                if arr[row][col]:
                    if col == n-1:
                        temp[row][col] = arr[row][col]
                    else:
                        k = 1
                        while (col+k) < n:
                            if temp[row][col+k] == 0:
                                flag = True
                                if (col+k) == n-1:
                                    temp[row][col+k] = arr[row][col]
                                    break
                                k += 1
                            else:
                                if temp[row][col+k] == arr[row][col]:
                                    if not visited[row][col+k]:
                                        flag = True
                                        visited[row][col+k] = True
                                        temp[row][col+k] += arr[row][col]
                                    else:
                                        if k > 1:
                                            flag = True
                                        temp[row][col+k-1] = arr[row][col]
                                else:
                                    if k > 1:
                                        flag = True
                                    temp[row][col+k-1] = arr[row][col]
                                break
    # 종료 처리
    if depth == 5 or not flag:
        max_num = 0
        for row in range(0, n):
            for col in range(0, n):
                if temp[row][col]:
                    if temp[row][col] > max_num:
                        max_num = temp[row][col]
        if answer < max_num:
            answer = max_num
        return
    for i in range(0, 4):
        dfs(depth+1, temp, i, n)


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
# 상 하 좌 우
answer = 0
for i in range(0, 4):
    dfs(1, MAP, i, N)
print(answer)