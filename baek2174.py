import sys
sys.stdin = open("baek2174.txt")


"""
A, B (가로, 세로) <= 100
N, M (로봇 갯수, 명령 갯수) <= 100,
따라서 시간적으로 여유가 충분함.

각 로봇은 초기 위치와 방향을 갖고 있음.
이 때 M개의 명령을 순차적 실행하며
각 명령은 L / R / F 중 한종류만, 하나의 로봇에 대해서만 실행 가능함.
(L 왼쪽 90도 회전, R 오른쪽 90도 회전, F 해당 방향으로 1칸 전진)

만약 모든 로봇이 정상적으로 실행되면 OK 출력,
충돌이 발생한 경우 (맵 밖으로 벗어났거나, 다른 로봇과 충돌)
가장 먼저 발생한 문제에 대해 출력
"""

def simulationRobot(robots, commands, r, c):
    
    # 북 동 남 서  (문제 기준이다, 여기서 북쪽은 row가 커지는 방향!)
    # 오른쪽 회전은 (현재 + 이동 횟수) % 4 이 다음 방향
    # 왼쪽 회전은 현재 - (이동 횟수) % 4 가 다음방향
    dirR = [1, 0, -1, 0]
    dirC = [0, 1, 0, -1]

    for i in range(0, len(commands)):
        target, command, loopCnt = commands[i]

        # 매번 하나의 로봇에 대해서만 명령
        now_row, now_col, now_dir = robots[target]
        if command == "L":
            # 왼쪽으로 인덱스 탐색할때 이렇게 쓰는거 익혀두자!
            next_dir = ((now_dir+4) - (loopCnt)%4)%4
            robots[target] = [now_row, now_col, next_dir]
        elif command == 'R':
            next_dir = (now_dir + loopCnt)%4 
            robots[target] = [now_row, now_col, next_dir]
        else:
            field = [[0] * c for _ in range(0, r)]
            # 충돌 체크 용
            for j in range(0, len(robots)):
                row, col, d = robots[j]
                field[row][col] = j+1

            row, col, direct = robots[target]
            for j in range(1, loopCnt+1):
                next_row = row + (dirR[direct]*j)
                next_col = col + (dirC[direct]*j)

                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    return f"Robot {target+1} crashes into the wall"
                # 가는 경로에 로봇이 있는경우 체크해야 함 
                if field[next_row][next_col]:
                    oppenent = field[next_row][next_col]
                    return f"Robot {target+1} crashes into robot {oppenent}"
            # 갱신해 주어야함!
            robots[target] = [next_row, next_col, direct]
    return "OK"

# 가로(col), 세로(row)
A, B = map(int, input().split())
N, M = map(int, input().split())
robots = [0] * N
commands = [0] * M
convertStrToIdx = {"N": 0, "E": 1, "S": 2, "W": 3}
for i in range(0, N):
    # 가로, 세로, 방향 문제 잘 읽자
    c, r, d = input().split()
    row = int(r) - 1
    col = int(c) - 1
    initDir = convertStrToIdx[d]
    robots[i] = [row, col, initDir]

for i in range(0, M):
    num, command, loopCnt = input().split()
    commands[i] = (int(num)-1, command, int(loopCnt))
answer = simulationRobot(robots, commands, B, A)
print(answer)