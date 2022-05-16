import sys
sys.stdin = open("baek17825.txt")
sys.setrecursionlimit(10**5)
"""
인덱스기준
기본적으로는 0열에서 진행
첫 스타트를 1행으로 했음!
5에 도착 => 1열로 이동해서 진행
10에 도착 => 2열로 이동해서 진행로 진행
15에 도착 => 3열로 이동해서 진행

매 횟수마다 최대 이동 칸수가 주어지므로, 매 경우의 수를 모두 따져보아야 한다.
도착하지 않은 말 (사용 가능한 말) 들에 대해서 
나온 주사위 칸만큼 이동하는 경우를 따짐
=> 따라서 현재 말들의 상황을 체크 가능해야 함
=> 어디의 위치인지, 그리고 위 경우중에서 어떤 루트를 갖고 가는지 (row값을 어떤값을 가지는지) 저장하고 있어야함
=> 다음 반복을 위해, 바로 리스트를 넘길게 아니고 ,깊은 복사를 해서 넘긴다.
4개의 말에대해서, 10 라운드를 하기에 충분히 가능하다고 생각
이건 풀고나서도 다른분들 풀이한번 보자..

막판에 25, 30, 35, 40 이부분에서 겹치는지 체크해야한다.. 
이걸 놓쳤네..
0인경우에는 goal-1
1, 2, 3인 경우에는 goal-4 ~ goal-1 까지가 겹칠 수 있다. 이걸 전부 체크해줘야함

이걸 그래프로 푸네 ㄷㄷㄷ
이렇게 경로를 복잡하게 따져야 하는경우는 그래프를 떠올릴 수 있어야 한다!!!
이런 문제를 혼자 풀 수 있을때까지... 계속해서 정진!!
복잡한 경로에 대한 문제는 => 그래프 + 인접행렬로 접근하자!!
"""

def find_max(round, point, horse, test, dice):
    global answer
    if round == 10:
        if point > answer:
            answer = point
        return
    move = dice[round]
    for i in range(0, 4):
        now = horse[i]
        # 분기점에 도착해 있는 경우 1번이동
        if len(graph[now]) == 2:
            now = graph[now][1]
        else:
            now = graph[now][0]
        # 남은 횟수 이동
        for j in range(1, move):
            now = graph[now][0]
        # now 가 32 즉 도착한 경우는 겹쳐도 상관 없다
        if now < 32:
            # 도착 전에서, 겹치는 경우
            if now in horse:
                continue
        before = horse[i]
        horse[i] = now
        test.append(now)
        find_max(round+1, point+score[now], horse, test, dice)
        test.pop()
        horse[i] = before
        
# score를 먼저 만들고, 그 위치에 맞추어 그래프 선언 score 32까지
# 이렇게 경로랑, 해당 경로에 점수를 어떻게 이렇게 연동할 생각을 한다냐 ㅡㅡ 대단하네
nums = list(map(int, input().split()))                                                                      #16    17   18     19    20    21    22    23    24    25    26   27     28    29   30     31    32
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
#                                                                                   20  21 22   23  24  25  26  27  28  29  30  31  32 (인덱스값이) 
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
answer = 0
pos = [0] * 4
find_max(0, 0, pos, [], nums)
print(answer)
