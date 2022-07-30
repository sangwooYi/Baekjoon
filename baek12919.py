"""
1. 뒤에 A 추가
2. 뒤에 B 추가 후 뒤집기
얘는 길이도 50까지밖에 안주었으며,
12904와는 다르게 작업 순서에 따라 답을 놓칠 수 가 있다.
(친절하게 예제에서 보여줌 A / BABA 인 경우)

그런데 똑같이 T -> S로 가는 방식으로
(S -> T는 고려할게 너무 많다.)
"""

def dfs(now, goal):
    global answer
    if len(now) == len(goal):
        return

    if now[-1] == "A":
        tmp = now[:-1]
        if len(tmp) == len(goal):
            if tmp == goal:
                answer = 1
                return
        dfs(tmp, goal)
    if now[0] == "B":
        tmp = []
        for i in range(len(now)-1, 0, -1):
            tmp.append(now[i])
        if len(tmp) == len(goal):
            if tmp == goal:
                answer = 1
                return
        dfs(tmp, goal)

S = list(input())
T = list(input())

answer = 0
dfs(T, S)
print(answer)