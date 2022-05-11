import sys
sys.stdin = open("baek20055.txt")

"""
매 단계 진행
1. 컨베이어 한칸씩 이동
2. 이동 가능한 로봇 회전방향으로 이동, 가장 먼저 벨트에 올라간 로봇부터! (이게 핵심이네.)
=> 이동가능 조건, 이동하려는 곳에 로봇이 없어야하며, 이동하려는 칸의 내구도가 1이상
3. 로봇을 올리는 칸 (1번칸)의 내구도가 1 이상이면 로봇을 올린다.
4. 내구도 0인 칸이 K개 이상이면 종료, 아니면 다시 1번으로'

컨베이어 내구도는 => 로봇이 해당칸으로 오거나, 1번칸에서 로봇이 올라올때
위 조건을 구현하면 됨.
"""

def find_step(arr, n, k):
    # 처음이 1단계
    result = 1
    # 로봇이 올라간 위치를 표시하기 위함
    robot = [False] * n
    while True:
        # 1단계 컨베이어 이동, 로봇도 같이 이동
        temp = arr[2*n-1]
        for i in range(2*n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
        # 로봇은 인덱스 N-1부터 0 사이에밖에 존재하지않는다
        if robot[n-1]:
            robot[n-1] = False
        for i in range(n-1, 0, -1):
            robot[i] = robot[i-1]
        # 이 처리 해줘야함, 이동했으므로 0번인덱스는 비어야함
        robot[i-1] = False
        # 내리는 칸에온 로봇 내림 
        if robot[n-1]:
            robot[n-1] = False
        # 2단계 이동가능한 로봇 확인하여 이동시킴, n번칸에서 내리므로 0부터 n-1까지만 보면 된다.
        # 가장 먼저 올라간 로봇부터 체크함
        for i in range(n-2, -1, -1):
            # 로봇이 있는 경우에만 체크
            if robot[i]:
                # 이동하려는칸에 로봇이 있는경우
                if robot[i+1]:
                    continue
                # 이동하려는 칸의내구도가 0인 경우
                if arr[i+1] == 0:
                    continue
                # 이동 가능한 경우 로봇 이동
                robot[i+1] = robot[i]   
                robot[i] = False
                # 내구도 감소
                arr[i+1] -= 1
                # 내리는칸에 온 로봇 내림
                if robot[n-1]:
                    robot[n-1] = False
        # 3단계 올리는 칸에 내구도가 1이상이면 로봇 올린다.
        if arr[0] > 0:
            robot[0] = True
            arr[0] -= 1
        # 내구도 체크
        count = 0
        for i in range(0, 2*n):
            if arr[i] == 0:
                count += 1
        # 종료조건
        if count >= k:
            return result
        # 다음 step으로
        result += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
answer = find_step(A, N, K) 
print(answer)