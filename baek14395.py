from collections import deque

A, B = map(int, input().split())

# 10**9 까지 존재
# 줄이는 방법으로는 빼서 0 , 나누어서 1로 만드는방법밖에는 없음 따라서 T 초과하면 사실 의미 X


upper_bound = max(A, B)
def bfs():

    # 리스트를 쓰면 10**9일때 메모리 초과 발생.. 10억바이트면 1GB임..
    visit_map = {}
    que = deque()

    # 애초에 사전순으로 배열
    oper_str = ["*", "+", "-", "/"]

    min_len = 9876543421
    visit_map[A] = 1
    que.append((A, ""))

    while que:
        cur_num, cur_str = que.popleft()

        
        if cur_num == B:
            return cur_str
        if len(cur_str) >= min_len:
            continue
        
        for i in range(0, 4):
            cur_oper = oper_str[i]
            if cur_oper == "*" and cur_num == 0:
                continue
            if cur_oper == "*":
                next_num = cur_num*cur_num
            elif cur_oper == "+":
                next_num = cur_num+cur_num
            elif cur_oper == "-":
                next_num = 0
            elif cur_oper == "/":
                next_num = 1
            if next_num > B:
                continue
            if next_num in visit_map.keys():
                continue
            visit_map[next_num] = 1
            next_str = cur_str+cur_oper
            que.append((next_num, next_str))
    return -1


if A == B:
    print(0)
else:
    ans = bfs()
    print(ans)