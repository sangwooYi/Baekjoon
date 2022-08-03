import sys
sys.stdin = open("baek2138.txt")

"""
i번 클릭시 , i-1, i, i+1번 상태 변경
단 1번은 1, 2번, N번은 N-1, N번이 변경됨

아이디어!!!! 

Case를 쪼개서 생각
1) 0번 전구를 누를때

2) 0번 전구를 누르지 않았을 때

0번 전구가 결정된 상태라면
=> 0번 전구의 상태는 1번전구만 결정 가능
=> 따라서 0번 전구가 원하는 상태와
   같으면 1번  안누름 / 다르면 1번 누름
   
   다음 step에서 1번전구에 영향은 2번만 줄 수 있음
   따라서 원하는 상태와
   같으면 2번 안누름 / 다르면 2번 누름
이렇게 순회해서 1, 2번 중 원하는 상태와 같으며, 둘다 가능하면 둘중 최솟값 출력 

이런 아이디어를 혼자 생각할 수 있어야 한다!
"""

N = int(input())
states = list(map(int, input()))
goal = list(map(int, input()))

case1 = -1
case2 = -1
# 0번 안누름
case1_arr = [0] * N
for i in range(0, N):
    case1_arr[i] = states[i]

cnt = 0
for i in range(0, N-1):
    # 다르면 i+1번 전구 누름
    if case1_arr[i] != goal[i]:
        cnt += 1
        case1_arr[i] = (case1_arr[i]+1) % 2
        case1_arr[i+1] = (case1_arr[i+1]+1) % 2
        if i < N-2:
            case1_arr[i+2] = (case1_arr[i+2]+1) % 2

if case1_arr == goal:
    case1 = cnt
# 0번 누름
case2_arr = [0] * N
for i in range(0, N):
    case2_arr[i] = states[i]
case2_arr[0] = (case2_arr[0]+1) % 2
case2_arr[1] = (case2_arr[1]+1) % 2

cnt = 1
for i in range(0, N-1):
    # 다르면 i+1번 전구 누름
    if case2_arr[i] != goal[i]:
        cnt += 1
        case2_arr[i] = (case2_arr[i]+1) % 2
        case2_arr[i+1] = (case2_arr[i+1]+1) % 2
        if i < N-2:
            case2_arr[i+2] = (case2_arr[i+2]+1) % 2

if case2_arr == goal:
    case2 = cnt

if case1 == -1 and case2 == -1:
    print(-1)
elif case1 == -1:
    print(case2)
elif case2 == -1:
    print(case1)
else:
    print(min(case1, case2))