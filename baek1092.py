import sys
sys.stdin = open("baek1092.txt")

"""
아래처럼 브루트포스로 하면 시간초과난다.
내가 한것은 매번 0 ~ m 까지를 반복한 로직이었는데,
position을 통해, 현재 크레인의 위치를 저장함으로써
불필요한 반복을 제거 가능함!
(옮길 수 있으면 visited 처리 하고 크레인 다음 위치로,
못 옮기는 경우는, 옮길 수 있는애가 나올떄까지 현재 크레인 위치를 계속 다음 위치로 이동 시켜주면 됨)
"""


def ship(arr, goods, n, m):
    # 화물 실었는지 체크 용
    visited = [False] * m

    flag = False
    result = 0
    count = 0
    # 이게 포인트다!
    # 현재 크레인의 위치를 저장! (이런 생각을 왜 못하냐 ㅠㅠ)
    position = [0] * n

    # 애초에 못 싣는 경우
    if goods[0] > arr[0]:
        return -1
    while count < m:
        for i in range(0, n):
            upper = arr[i]
            # 위치
            while position[i] < m:
                # # 싣는게 가능한 경우 (이런식으로 로직을 짜는게 훨씬 간단하다!)
                # if not visited[position[i]] and upper >= goods[position[i]]:
                #     count += 1
                #     visited[position[i]] = True
                #     position[i] += 1
                #     break
                # # 불가능한 경우는 포지션만 변경
                # position[i] += 1
                # 이건 내 습관 (상관은 없다!)
                if visited[position[i]] or upper < goods[position[i]]:
                    position[i] += 1
                else:
                    count += 1
                    visited[position[i]] = True
                    position[i] += 1
                    break
        result += 1
    return result

N = int(input())
crane = list(map(int, input().split()))
# 내림차순
crane.sort(key=lambda x : -x)
M = int(input())
cargo = list(map(int, input().split()))
cargo.sort(key=lambda x: -x)

answer = ship(crane, cargo, N, M)
print(answer)