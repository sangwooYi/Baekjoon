import sys
from collections import deque
sys.stdin = open("baek13335.txt")


# 트럭수, 다리길이, 하중
N, W, L = map(int, input().split())
truck = list(map(int, input().split()))


cur_weight = 0
total_time = 0
idx = 0


que = deque()
while True:
    tmp_que = deque()
    while que:
        weight, length = que.popleft()
        next_length = length+1
        if next_length > W:
            cur_weight -= weight
        else:
            tmp_que.append((weight, next_length))

    if idx < N:
        next_weight = cur_weight + truck[idx]
        if next_weight <= L:
            cur_weight = next_weight
            tmp_que.append((truck[idx], 1))
            idx += 1
    while tmp_que:
        tmp_weight, tmp_length = tmp_que.popleft()
        que.append((tmp_weight, tmp_length))
    total_time += 1
    if not que:
        break

print(total_time)