import sys
sys.stdin = open("baek11067.txt")

"""
우선 x축기준으로 오름차순 정렬
같은 x축좌표를 가진 친구들 => 그다음 x좌표로넘어갈때 
경로를 어떻게 잡는지가 핵심

우선 모노톤길을 보장해주는 문제기때문에
현재 기준으로 y축으로는 커지거나 or 작아지거나만 가능.
따라서 우선 x축 커지는 방향으로 체크
=> x축이 같은 친구들끼리는 현재 위치가 가장 작거나 or 가장 큰 경우인것.
=> 그다음 x가 커지는 방향으로 진행시에는 y축이 같은 친구가 무조건 존재
이걸 계속 반복하며 진행
"""

def make_monotone(nodes_info, count_dict):
    
    total_cnt = len(nodes_info)
    
    result = [0] * total_cnt
    idx = 0
    # 같은 x좌표를 갖는 노드중 마지막 경로에 위치한 y좌표
    last_y = 0
    x_coords = list(count_dict.keys())
    x_coords.sort()
    
    for i in range(0, len(x_coords)):
        cur_x = x_coords[i]
        cur_cnt = count_dict[cur_x]

        # 그냥 한개일때는 바로 진행
        if cur_cnt == 1:
            result[idx] = nodes_info[idx]
            last_y = nodes_info[idx][1]
        else:
            cur_min_y = nodes_info[idx][1]
            cur_max_y = nodes_info[idx+cur_cnt-1][1]
            # y좌표 내림차순 진행
            if last_y == cur_max_y:
                for j in range(0, cur_cnt):
                    result[idx+j] = nodes_info[idx+cur_cnt-1-j]
                last_y = cur_min_y
            # y좌표 오름차순 진행
            else:
                for j in range(0, cur_cnt):
                    result[idx+j] = nodes_info[idx+j]
                last_y = cur_max_y
        idx += cur_cnt

    return result



T = int(sys.stdin.readline())
for tc in range(0, T):
    N = int(sys.stdin.readline())
    nodes = [0] * N
    # x좌표가 동일한 노드가 각각 몇개씩 존재하는지 체크
    count_dict = {}
    for i in range(0, N):
        x, y = map(int, sys.stdin.readline().split())
        nodes[i] = [x, y]
        if x not in count_dict.keys():
            count_dict[x] = 1
        else:
            count_dict[x] += 1

    # 우선 x좌표 오름차순 y좌표 오름차순으로 정렬
    nodes.sort(key=lambda x : (x[0], x[1]))
    result = make_monotone(nodes, count_dict)
    
    tmp = list(map(int, sys.stdin.readline().split()))
    chk_node_cnt = tmp[0]
    chk_nodes = tmp[1:]
    for chk_node in chk_nodes:
        print(f"{result[chk_node-1][0]} {result[chk_node-1][1]}")