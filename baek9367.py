import sys
import math
sys.stdin = open("baek9367.txt")


"""
내풀이는 왜 틀리는데 ㅡㅡ?

p 는 대여
r 는 반납 ( 초기대여료 + km당 추가요금)
a 는 사고 (사고는 파손율*원가 만큼 비용 추가
=> 소숫점은 그냥 올림처리)

첩보원 dict는
일관성여부 flag, 차보유 flag, 현재까지 비용
을 정보로 갖고 있는다.

일관성여부 flag 가 false면 그냥 계속 pass

일관성여부 체크
=> 1. 차보유 flag가 true인데 p (대여)를 함  
   2. 차보유 flag가 false 인데 p (대여) 나 a(사고) 가 남
   3. 마지막에 차를 반납 안한상태면 (차보유 flag가 true로 끝나면)

일관성이 유지되어있다면
=> 반납시: 초기 대여료 + km*추가요금 +  (현재까지수리비 반올림) 만큼 비용 가산
   사고시: 원가*파손율 만큼을 사고 비용에 추가
=> 첩보원 dict key 오름차순으로 정렬후
일관성여부 true면 금액 / false면 "INCONSISTENT" 출력   
"""


price = "price"
init_cost = "init_cost" 
add_cost = "add_cost"


T = int(sys.stdin.readline().rstrip())
for tc in range(0, T):
    car_info_dict = {}
    spy_dict = {}
    N, M = map(int, sys.stdin.readline().split())
    
    for i in range(0, N):
        # 차이름 원가, 초기대여비용, km당 추가요금
        car_name, car_price, initial_cost, additional_cost = sys.stdin.readline().split()
        # 원가, 초기 대여료, km당 추가요금 
        car_info_dict[car_name] = {
            price: int(car_price),
            init_cost: int(initial_cost),
            add_cost: int(additional_cost)
        }

    for i in range(0, M):
        # 시간순, 첩보원명, 구분자(p, r, a), 요소 (금액 or 차명)
        time_line, name, seper, elem = sys.stdin.readline().split()

        if name in spy_dict.keys():
            # 일관성 유지될 때만 진행
            if spy_dict[name][0]:
                # 대여
                if seper == "p":
                    # 이미 갖고있는데 또 대여
                    if spy_dict[name][1]:
                        spy_dict[name][0] = False
                    else:
                        spy_dict[name][1] = True
                        spy_dict[name][2] = elem
                else:
                    # 차 없는데 사고나거나 반납하라면 일관성 X
                    if not spy_dict[name][1]:
                        spy_dict[name][0] = False
                    else:
                        cur_car = spy_dict[name][2]
                        # 반납
                        if seper == "r":
                            mileage = int(elem)
                            # 초기 대여료 + 추가요금*km
                            req_cost = car_info_dict[cur_car][init_cost] + (mileage*car_info_dict[cur_car][add_cost])
                            spy_dict[name][3] += req_cost

                            # 초기화
                            spy_dict[name][1] = False
                            spy_dict[name][2] = ""

                        # 사고
                        else:
                            damage_rate = int(elem)/100
                            tmp_rep = car_info_dict[cur_car][price]*damage_rate
                            repair_cost = math.ceil(tmp_rep)
                            spy_dict[name][3] += repair_cost
        else:
            # 초깃값은 [True, False, "", 0] (일관성 유지, 차보유 X, 차 이름 초기화, 총 비용 0원)
            spy_dict[name] = [True, False, "", 0]
            
            # 초기 등장 때는 p (대여) 만 가능
            # 만약 r (반납) or  a (사고) 면 일관성 깨짐
            if seper == "r" or seper == "a":
                spy_dict[name][0] = False
            else:
                spy_dict[name][1] = True
                spy_dict[name][2] = elem

    spies_arr = list(spy_dict.keys())
    spies_arr.sort()
    for i in range(0, len(spies_arr)):
        cur_spy = spies_arr[i]
        
        if spy_dict[cur_spy][1]:
            spy_dict[cur_spy][0] = False

        if spy_dict[cur_spy][0]:
            print(f"{cur_spy} {spy_dict[cur_spy][3]}")
        else:
            print(f"{cur_spy} INCONSISTENT")