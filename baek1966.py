import sys
sys.stdin = open("baek1966.txt")

"""
어차피 N, M 범위가 100까지밖에안되니, 
주어진 우선순위 배열을 정렬하여 현존하는 최대 우선순위값을 계속 체크한다.
해당 우선순위값이 나올떄까지 계속 디큐, 엔큐 반복
나왔으면 그제서야 디큐만. 그리고 그떄 order + 1
우리가 원하는 값이면 그 후 return

못찾는경우는 절대 없음

arr.pop(0)  디큐랑 똑같고
arr.append() 엔큐 제일끝단에 넣는거
"""


def when_print(arr, idx):
    # 찾으려는 문서가 현재 어디있는지 체크용
    find = [False] * len(arr)
    find[idx] = True

    # 깊은복사 (우선순위)
    # 우선순위 체크용 배열 복사후 정렬
    check = [0] * len(arr)
    for i in range(0, len(check)):
        check[i] = arr[i]
    # 정렬
    check.sort()
    
    # 출력 순서
    order = 0
    while arr:
        # 현재 남아있는 최대 우선순위
        max = check[len(check) - 1]
        # 현재 출력 대기 문서 pop(0)
        now = arr.pop(0)
        now_flag = find.pop(0)
        # 아직 더 큰 출력범위가 있으면 맨 뒤로 보냄
        if now < max:
            arr.append(now)
            find.append(now_flag)

        else:
            # 가장 높은 우선순위면 출력
            order += 1
            # 현재 출력한게 찾으려는 문서가 맞다면 그떄 order값 반환
            if now_flag:
                return order
            # 찾으려는 문서가 아니면 계속 진행
            # 우선순위 체크용 배열도 조작 
            check.pop()
            

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    NUMS = list(map(int, input().split()))  
    answer = when_print(NUMS, M)
    print(answer)