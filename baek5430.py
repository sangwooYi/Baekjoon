import sys
sys.stdin = open("baek5430.txt")



def after_ac(inst, target):
    for i in range(0, len(inst)):
        if inst[i] == "D":
            if len(target):
                # 디큐처럼 0번 인덱스 제거하는것
                target.pop(0)
            else:
                return "error"
        elif inst[i] == "R":
            for i in range(0, len(target) // 2):
                temp = target[i]
                target[i] = target[len(target) - 1 -i]
                target[len(target) -1  -i] = temp
    result = "["
    for i in range(0, len(target)):
        if i == len(target) - 1:
            result += (target[i] + "]")
        else:
            result += (target[i] + ",")
    return result

T = int(input())
for tc in range(1, T+1):
    P = list(input())
    N = int(input())
    in_arr = input()
    arr = in_arr[1:-1].split(",")
    # 빈리스트 처리 한번 더
    if arr[0] == '':
        arr = []
    answer = after_ac(P, arr)
    print(answer)