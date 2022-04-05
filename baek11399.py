import sys
sys.stdin = open("baek11399.txt")

"""
기다리는 시간이 최소가 되려면
=> 빨리 끝나는 애부터 처리하면 된다. 
=> why? 처리시간이 긴애가 처음에나오면, 나머지 사람들도 그 시간만큼 같이 기다리므로 총량 증가!
=> 전형적인 그리디 문제
"""

N = int(input())
P = list(map(int, input().split()))
P.sort()
answer = 0
cost = 0
for i in range(0, len(P)):
    cost += P[i]
    answer += cost
print(answer)