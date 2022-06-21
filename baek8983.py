import sys
sys.stdin = open("baek8983.txt")

"""
거리는 그냥 
발사대는 (x1, 0) 동물 위치는 (x2, y2)라면
|x1-x2| + y2 로 정의함


각 동물을 순회하면서

각 동물 위치마다 =>
거리 <= 사거리 조건을 만족하는 발사대가 있는지 이분탐색

=> 조건 들어오면 count += 1
없으면 pass

복잡도는 O(NlogN), 10만개 sort도 NlogN이므로 
NlogN + NlogN  = O(NlogN)
"""

# 발사대는 어차피 y좌표가 0
def distance_between(ax, bx, by):
    return (abs(ax-bx) + by)


def count_possible(animals, shoot_points, m, n, l):
    count = 0
    # 모든 동물에 대해 탐색
    for i in range(0, n):
        x, y = animals[i]
        
        pl = 0
        pr = m-1
        while pl <= pr:
            mid = (pl + pr) // 2
            # 현재 발사대 위치            
            px = shoot_points[mid]
            distance = distance_between(px, x, y)
            # 사정거리 안에 들어왔으면 그냥 종료
            if distance <= l:
                count += 1
                break
            # x < px 면 pr = mid-1, x > px 면 pl = mid+1, x == px면 종료 (이게 최단거리임..)
            if x < px:
                pr = mid-1
            elif x > px:
                pl = mid+1
            else:
                break
    return count


# 사대 갯수, 동물 수, 사거리
M, N, L = map(int, input().split())

# 발사대 y좌표는 전부 0
points = list(map(int, input().split()))

# 사대 위치 오름차순 정렬
points.sort()


# 각 동물의 x,y 좌표 존재
animals = [0] * N
for i in range(0, N):
    animals[i] = list(map(int, input().split()))

answer = count_possible(animals, points, M, N, L)
print(answer)