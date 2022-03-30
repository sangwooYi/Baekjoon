import sys
import heapq
sys.stdin = open("baek7662.txt")
"""
이 문제는 꼭 한번더 풀어보자!
최소힙 / 최대힙 한방향으로만 하는것은 쉽지만
둘을 번갈아가면서 써야하는경우 아래와 같은 아이디어를 쓸 수 있는것


i 번째 연산에 대한 수를 넣었으면 visited[i] 를 True로 바꾸어주고
각각 delete처리를 해야할 때,
최대 힙이면, 현재 루트 값이 처리가 되었는지를 체크,
처리된애라면 처리 아직 안된애가 나올때까지 pop (while que_max and not visited[que_max[0][1]])
그다음 pop하고 그 연산순서에 해당하는 visited False로 변환
최소힙도 같은 로직으로 처리
전부 처리후에, que_max, que_min 둘다, 루트노드의 값중에 이미 처리 되었는데
남아있는애가 없나 체크해서 버린다.
"""


T = int(sys.stdin.readline())
answer = [0] * T
for tc in range(0, T):
    K = int(sys.stdin.readline())
    que_min = []
    que_max = []
    data = 0
    # K번쨰 연산에서 삽입한 수가 남아있는지 체크용
    visited = [False] * K
    for i in range(0, K):
        oper, num = sys.stdin.readline().split()
        num = int(num)
        if oper == "I":
            visited[i] = True
            # 최대힙으로 만드려면 -곱해서 저장한다. 그리고 몇번째 연산인지를 저장
            heapq.heappush(que_max, (-num, i))
            heapq.heappush(que_min, (num, i))
        elif oper == "D":
            if num == 1:
                # que_max에서 가장 앞의요소가 이미 처리됬다면, 
                # 처리 안된애가 나올떄까지 pop을 해준다 (상태를 맞추어주는것!)
                while que_max and not visited[que_max[0][1]]:
                    heapq.heappop(que_max)
                # 그래도 남아있다면
                if que_max:
                    now = heapq.heappop(que_max)
                    visited[now[1]] = False
            elif num == -1:
                # que_max와 동일
                while que_min and not visited[que_min[0][1]]:
                    heapq.heappop(que_min)
                if que_min:
                    now = heapq.heappop(que_min)
                    visited[now[1]] = False
    
    # 위의 처리를 한 후에, 그다음 상태 맞춰주는 처리
    while que_min and not visited[que_min[0][1]]:
        heapq.heappop(que_min)

    while que_max and not visited[que_max[0][1]]:
        heapq.heappop(que_max)
    
    # 한쪽이라도 비어있으면 결국 전부 비어있는 결과가 나오는게 맞는것
    # 한 자료에대해 병렬적으로 진행한것이므로!
    if len(que_min) == 0 or len(que_max) == 0:
        print("EMPTY")
    else:
        print(-que_max[0][0], end=" ")
        print(que_min[0][0])