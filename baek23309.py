import os, io, sys
sys.stdin = open("baek23309.txt")

"""
간이 리스트 형태로 선언
해당 고유 번호 값에 해당하는 노드는 이전역 / 다음역 정보를 갖는다

BN : i 번 노드의 다음역 k 출력 후 
i번 노드 다음역을 j로, k번 노드 이전역을 j로 업데이트
j 번 은 이전역은 i번, 다음역은 k가 됨

BP : i번 노드의 이전역 k를 출력 후
i번 노드의 이전역을 j로 k번 노드 다음역을 j 로
j 번은 이전역은 k, 다음역은 i가 됨

CN : i번 노드의 다음역 k 출력후 해당 k의 다음역 l 을 i의 다음역으로 업데이트
l 의 이전역을 i로 업데이트, 

CP : i번 노드의 이전역 k 출력호, k의 이전역을 i의 이전역 l로 , l의 다음역을
i로, 

방법은 맞는데 파이썬으로 시간초과 ㅡㅡ
"""

N, M = map(int, sys.stdin.readline().split())
init_stations = list(map(int, sys.stdin.readline().split()))

# 각 노드는 고유번호를 의미, 본인 기준 이전 역, 다음 역에대한 고유 번호 정보를 갖게 한다
# 원래 제대로 리스트 구조를 만드는게 좋긴 함 512MB이니까 충분
list_arr = [[0] * 2 for _ in range(0, 12)]

for i in range(0, N):

    pre_station_idx = i-1
    next_station_idx = i+1
    if pre_station_idx < 0:
        pre_station_idx = N-1
    if next_station_idx >= N:
        next_station_idx = 0
    
    node = init_stations[i]

    list_arr[node][0] = init_stations[pre_station_idx]
    list_arr[node][1] = init_stations[next_station_idx]


for i in range(0, M):
    tmp = list(sys.stdin.readline().split())

    oper = tmp[0]
    if oper == "BN":
        i, j = map(int, tmp[1:])

        next_node = list_arr[i][1]
        print(next_node)

        list_arr[i][1] = j
        list_arr[next_node][0] = j

        list_arr[j][0] = i
        list_arr[j][1] = next_node

    elif oper == "BP":
        i, j = map(int, tmp[1:])
        
        prev_node = list_arr[i][0]
        print(prev_node)

        list_arr[i][0] = j
        list_arr[prev_node][1] = j
        
        list_arr[j][0] = prev_node
        list_arr[j][1] = i

    elif oper == "CN":
        i = int(tmp[1])

        next_node = list_arr[i][1]
        print(next_node)
        next_next_node = list_arr[next_node][1]

        list_arr[i][1] = next_next_node
        list_arr[next_next_node][0] = i

    elif oper == "CP":
        i = int(tmp[1])
        prev_node = list_arr[i][0]
        print(prev_node)
        prev_prev_node = list_arr[prev_node][0]

        list_arr[i][0] = prev_prev_node
        list_arr[prev_prev_node][1] = i
