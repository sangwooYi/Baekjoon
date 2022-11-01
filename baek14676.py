import sys
sys.stdin = open("baek14676.txt")

"""
지을수 없는데 짓는다던가
(in_order 가 0이아닌데)

없는데 부수라는
(build_infos 가 0인것)
경우 중 하나라도 걸리면 바로 break 시키면 됨!

주의할 부분은, 중복건설이 가능하므로
build_infos가 0인 건물을 지을 때만 in_order 을 체크해주는 부분!
"""

N, M, K = map(int, sys.stdin.readline().split())
in_order = [0] * (N+1)
build_infos = [0] * (N+1)
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    in_order[b] += 1

answer = "King-God-Emperor"
for i in range(0, K):
    oper, node = map(int, sys.stdin.readline().split())
    # 건설
    if oper == 1:
        if in_order[node]:
            answer = "Lier!"
            break
        if build_infos[node] == 0:
            for next_node in graph[node]:
                in_order[next_node] -= 1
        build_infos[node] += 1

    # 파괴
    else:
        if build_infos[node] == 0:
            answer = "Lier!"
            break
        build_infos[node] -= 1
        if build_infos[node] == 0:
            for next_node in graph[node]:
                in_order[next_node] += 1
print(answer)