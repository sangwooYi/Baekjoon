import sys
from collections import deque
sys.stdin = open("baek3865.txt")

while True:
    N = int(input())
    if N == 0:
        break
    classes = [0] * N
    for i in range(0, N):
        classes[i] = input()
    
    class_dict = {}
    class_idx = {}
    class_member_list = [0] * N
    # 역으로 진행 (순환되는 구조로는 문제가 주어지지 않는다고 했음)
    for i in range(0, N):
        for j in range(0, len(classes[i])):
            if classes[i][j] == ":":
                class_name = classes[i][:j]
                tmp_list = classes[i][j+1:-1]
                break
        # 학회 이름은 전부 다르다
        member_list = tmp_list.split(",")
        class_dict[class_name] = {}
        class_idx[class_name] = i
        class_member_list[i] = [class_name, member_list]

    first_class_name = class_member_list[0][0]
    first_class_member = class_member_list[0][1]

    visited = [False] * N
    que = deque()
    que.append(first_class_name)
    visited[0] = True
    while que:
        # 무조건 학회명만 온다.
        now_class_name = que.popleft()
        idx = class_idx[now_class_name]
        member_list = class_member_list[idx][1]
        

        for member_name in member_list:
            if member_name not in class_dict.keys():
                if member_name in class_dict[first_class_name]:
                    continue
                class_dict[first_class_name][member_name] = 1
            else:
                next_idx = class_idx[member_name]
                if visited[next_idx]:
                    continue
                visited[next_idx] = True
                que.append(member_name)
    print(len(class_dict[first_class_name].keys()))
