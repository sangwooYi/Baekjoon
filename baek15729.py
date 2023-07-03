import sys
sys.stdin = open("baek15729.txt")


N = int(sys.stdin.readline().rstrip())
target = list(map(int, sys.stdin.readline().split()))

cur_arr = [0] * N
cnt = 0

"""
target 이 1이고, 현재가 0이면 눌러야 한다. => 그리고 뒤에 2칸도 변경
target 이 0이고, 현재가 1이어도 눌러야한다 => 그리고 뒤에 2칸도 변경
"""
for i in range(0, N):
    if target[i] == cur_arr[i]:
        continue
    # 우선 현재 위치의 값이 다를떄만 체크
    cnt += 1
    for j in range(0, 3):
        idx = i+j
        # 범위 벗어나면 종료
        if idx >= N:
            break
        # 1이면 0으로 0이면 1로
        cur_arr[idx] = (cur_arr[idx]+1)%2
print(cnt)

