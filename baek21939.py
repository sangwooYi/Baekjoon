import sys
import heapq
sys.stdin = open("baek21939.txt")

"""
지금까지 heapq를 잘못 생각하고 있었네 ㅡㅡ..
최대힙,
최소힙 우선순위큐를 각각 선언 (난이도 기준 최소힙, 최대힙)
+ 문제 번호 - T/F를 매핑한 딕셔너리를 만든다.

최대힙, 최소힙 각각, 이미 F처리된 애들은 pass 시키는 로직이
추가되야함.

add P L 은 최대힙, 최소힙에 각가 넣고,
문제번호 - T 를 딕셔너리에 추가해주면 됨

근데 추천에서
같은 난이도가 여러개인 경우, 가장 큰 /가장 작은 번호를 출력하는 로직도
들어가야 함.
1. 일단 recommend 때, 
같은 난이도 갖는 번호들 뽑은 후, 정렬해서 최소번호 찾는 로직으로?
=> 당연히 시간초과 난다.

파이썬에서 heapq는 디폴트 값이
무조간 0번 인덱스 기준으로 정렬하는것이 아니다!
0번요소 기준 최소힙 -> 0번요소가 같은 값들에 대해서는 1번 기준으로 다시 최소힙 ... 이런식으로 
자동으로 정렬해줌!!!!

ex) [[1, 4], [2, 5], [2, 3], [1, 2]] 이런 요소들이 있다면
heapify를 진행하고 나면
이 리스트에 0번 요소는 [1, 2] 가 된다 ! (완전 오름차순 정렬은 아니기 때문)
(0번 기준 최솟값 (1) 이 [1, 2], [1, 4] 가 존재하며, 이중에서 1번요소 최솟값은 [1, 2]기 때문!
이부분까지 자동으로 해주는게 heapq이다!)
"""

N = int(sys.stdin.readline())

# 최소힙
min_hq = []
# 최대힙 
max_hq = []

problem_dict = {}


for i in range(0, N):
    num, lev = map(int, sys.stdin.readline().split())
    # 이렇게 heapq에 넣으면 알아서, 가장 쉬운 문제 중에서 가장 작은 번호를 꺼내 줌
    heapq.heappush(min_hq, (lev, num))
    # 기본적으로 heapq 는 최소힙으로 구현 되어있음
    # 이렇게 넣어주면 알아서 가장 어려운 문제중에서 가장 큰 번호를 꺼내줌 ! 
    heapq.heappush(max_hq, (-lev, -num))
    problem_dict[num] = True

M = int(sys.stdin.readline())
for i in range(0, M):
    tmp = sys.stdin.readline().split()
    oper = tmp[0]
    if oper == "add":
        number = int(tmp[1])
        level = int(tmp[2])

        while True:
            lev, num = max_hq[0]
            if not problem_dict[-num]:
                heapq.heappop(max_hq)
            else:
                break
        while True:
            lev, num = min_hq[0]
            if not problem_dict[num]:
                heapq.heappop(min_hq)
            else:
                break
        heapq.heappush(min_hq, (level, number))
        heapq.heappush(max_hq, (-level, -number))
        problem_dict[number] = True

    elif oper == "solved":
        num = int(tmp[1])
        # 풀었으므로 False로 변경 (반드시 있는애만 주어짐)  
        problem_dict[num] = False

    else:
        # 최고난이도
        if tmp[1] == "1":
            while True:
                level, number = max_hq[0]
                if not problem_dict[-number]:
                    heapq.heappop(max_hq)
                else:
                    print(-number)
                    break

        # 최저난이도
        else:
            while True:
                level, number = min_hq[0]
                if not problem_dict[number]:
                    heapq.heappop(min_hq)
                else:
                    print(number)
                    break
