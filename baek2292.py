"""
이 문제에서
거리가 n 인것의 범위 
1 + 6*((n)*(n+1) //2)
"""
import sys
sys.stdin = open("baek2292.txt")

def find_min(num):
    if num == 1:
        return 1
    dist = 1
    while True:
        max_dist = 1 + 6*dist*(dist+1)//2
        if num > max_dist:
            dist += 1

        else:
            break
    # num 값이 max_dist값보다 같거나 작아지는 순간 stop 그떄 dist + 1 값이 가야할 거리
    return dist + 1

N = int(input())
answer = find_min(N)
print(answer)