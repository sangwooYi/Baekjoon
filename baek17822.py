import sys
sys.stdin = open("baek17822.txt")

"""
1. 요구사항에 맞추어 회전
시계방향 -> / 반시계방향 <- 
2. 회전 후에 인접하면서, 숫자 같은애들 있는지 전부 체크
   (한번에 삭제해야 하는것이 포인트)
3. 2번의 경우가 전혀 없는 경우라면 현재 평균을 구한 후, 평균보다 작으면 +1 크면 -1

이것만 잘 시행해주면 끝!
=> 만약 모든 숫자가 사라지면 그냥 종료!

주의할것, 인덱스 // 번호는 1부터 시작 이부분을 헷갈리지 말것
"""

def rullet(arr, opers, n, m, t):
    result = 0

    for i in range(0, t):
        # x배수의 원판을 d방향으로 k칸 회전 (d=0 시계, 1은 반시계)
        x, d, k = opers[i]

        for j in range(0, n):
            # 번호판과 인덱스 1차이
            th = j+1
            # x의 배수인 원판만 회전
            if (th % x) == 0:
                temp_arr = [0] * m
                # 반 시계 방향
                if d == 1:
                    for s in range(0, m):
                        if s < k:
                            z = (m-(k-s))
                            temp_arr[z] = arr[j][s]
                        else:
                            temp_arr[s-k] = arr[j][s]
                    arr[j] = temp_arr
                # 시계 뱡향
                else:
                    for s in range(0, m):
                        z = (s+k) % m
                        temp_arr[z] = arr[j][s]
                    arr[j] = temp_arr               

        # 회전 후, 인접하면서 숫자 같은애들 체크
        flag = False
        visited = [[False] * m for _ in range(0, n)]

        for r in range(0, n):
            for c in range(0, m):
                now = arr[r][c]
                # 숫자가 있을 때만 진행 (없는 숫자는 0으로 처리, 숫자 없을 경우는 그냥 pass)
                if now:
                    # 양 옆 체크
                    if c == 0:
                        right = c+1
                        left = m-1
                    elif c == m-1:
                        right = 0
                        left = c-1
                    else:
                        right = c+1
                        left = c-1

                    if arr[r][right] == now:
                        flag =  True
                        visited[r][c] = True
                        visited[r][right] = True
                    if arr[r][left] == now:
                        flag = True
                        visited[r][c] = True
                        visited[r][left] = True
                    
                    # 앞 뒤 체크
                    if r == 0:
                        if arr[r+1][c] == now:
                            flag = True
                            visited[r][c] = True
                            visited[r+1][c] = True
                    elif r == n-1:
                        if arr[r-1][c] == now:
                            flag = True
                            visited[r][c] = True
                            visited[r-1][c] = True
                    else:
                        front = r-1
                        rear = r+1
                        if arr[front][c] == now:
                            flag = True
                            visited[r][c] = True
                            visited[front][c] = True
                        if arr[rear][c] == now:
                            flag = True
                            visited[r][c] = True
                            visited[rear][c] = True
        # 인접하면서 숫자 같은애들 처리
        if flag:
            for r in range(0, n):
                for c in range(0, m):
                    # 인접하면서 숫자 같은애들 처리
                    if visited[r][c]:
                        arr[r][c] = 0
        # 인접하면서 숫자 같은애가 전혀 없는 경우
        else:
            tmp_sum = 0
            count = 0
            for r in range(0, n):
                for c in range(0, m):
                    # 숫자 있는경우만
                    if arr[r][c]:
                        tmp_sum += arr[r][c]    
                        count += 1
            if tmp_sum == 0:
                return 0
            avg = tmp_sum / count
            for r in range(0, n):
                for c in range(0, m):
                    if arr[r][c]:
                        if arr[r][c] > avg:
                            arr[r][c] -= 1
                        elif arr[r][c] < avg:
                            arr[r][c] += 1

    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j]:
                result += arr[i][j]
    return result

N, M, T = map(int, input().split())
MAP = [[] for _ in range(0, N)]
C = [0] * T
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
for i in range(0, T):
    C[i] = list(map(int, input().split()))

answer = rullet(MAP, C, N, M, T)
print(answer)