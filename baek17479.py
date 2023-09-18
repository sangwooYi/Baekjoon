import sys
sys.stdin = open("baek17479.txt")

def is_right_order(cnt_arr, cost_arr):

    #일반메뉴만 시킨 경우
    if cnt_arr[1] == 0 and cnt_arr[2] == 0:
        return True
    # 특별메뉴는 시킴
    if cnt_arr[1] > 0 :    
        # 일반메뉴 2만원 미만인경우, 안시킨경우도 여기에 포함 됨
        if cost_arr[0] < 20000:
            return False
        
    # 서비스 메뉴를 시킴
    if cnt_arr[2] > 0:
        # 위에서 한번 걸렀으므로, 특별메뉴를 시켰으면 시키는 조건은 만족해있는 상태
        if cost_arr[0] + cost_arr[1] < 50000:
            return False
        
        # 일반메뉴를 안시키는건 구조적으로 불가능
        if cnt_arr[0] == 0:
            return False

        # 1개까지만 주문 가능
        if cnt_arr[2] > 1:
            return False
    return True
        
          



A, B, C = map(int, input().split())

menus = {}

for i in range(0, A+B):
    menu, cost = input().split()

    menu_idx = 0
    if i >= A and i < A+B:
        menu_idx = 1
    menus[menu] = [menu_idx, int(cost)]

for i in range(0, C):
    menu = input()

    menus[menu] = [2]


menu_cnt = [0] * 3
menu_cost = [0] * 3

N = int(input())
for i in range(0, N):
    cur = input()
    
    menu_idx = menus[cur][0]

    menu_cnt[menu_idx] += 1

    if menu_idx < 2:
        menu_cost[menu_idx] += menus[cur][1]


flag = is_right_order(menu_cnt, menu_cost)

if flag:
    print("Okay")
else:
    print("No")