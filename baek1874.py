import sys
sys.stdin = open("baek1874.txt")

def make_stk(num, arr):
    # 스택이 있을때동안 계속 진행, 초깃값 세팅
    result = ["+"]
    stk = [1]
    i = 0
    now = 1
    # now가 num  이하일까지만 진행
    while now <= num:
        # 아직 안끝났는데 stk 비어 있으면
        if len(stk) == 0:
            now += 1
            # 현재 체크한 값이 이미 num 벗어나버렸으면 끝낸다.
            if now > num:
                break
            stk.append(now)
            result.append("+")
        # 스택의 가장 top의 숫자가 arr[i]와 같을때까지 push
        else:
            # stk[-1] .peek() arr[i] = value
            if stk[-1] != arr[i]:
                # 그리고 숫자를 계속 1씩 증가시킴
                now = now + 1
                stk.append(now)
                result.append("+")
            # 같으면 pop, i 1증가
            else:

                i += 1
                stk.pop()
                result.append("-")
    # 스택이 남아있으면 NO 반환, 불가능한것
    if stk:
        return "NO"
    # 스택이 비어있다면 result 반환
    return result

N = int(input())
ARR = []
for i in range(0, N):
    ARR.append(int(input()))
answer = make_stk(N, ARR)
# NO 반환시에 체크용
if type(answer) == str:
    print(answer)
else:
    for i in range(0, len(answer)):
        print(answer[i])