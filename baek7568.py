import sys
sys.stdin = open("baek7568.txt")
"""
50명 밖에안되므로, 일일이 비교하는것도 가능할듯?
or  (키, idx) 이런식으로 두고 정렬하여 위치를 비교하여 체크하는 방법도 좋을듯
나보다 덩치가 큰사람이 몇명인지 찾으면 된다.
4 같은경우는 키, 몸무게 둘다 내 앞에 4명 따라서 5등
2 같은경우는 키, 몸무게 둘다 내 앞에 0명 따라서 1등
3번은 키는 내앞에 3명, 몸무게는 내앞에 1명 => 이 사이에 세명은 우위가 없다.
"""

def calc_rate(mans, n):
    order = [0] * n
    
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            # 본인 제외
            if i == j:
                continue
            # 그냥 문제대로 ...
            if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
                count += 1
        order[i] = count + 1
        

    return order


N = int(input())
MAP = []
for i in range(0, N):
    temp = list(map(int, input().split()))
    MAP.append(temp)
answer = calc_rate(MAP, N)
for i in range(0, len(answer)):
    if i == len(answer) - 1:
        print(answer[i])
    else:
        print(answer[i], end=" ")