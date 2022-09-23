import sys
sys.stdin = open("baek13164.txt")

"""
K개 조로 나누어여 하며,
각 조의 티셔츠 제작비용은
그 조에서 최대키-최소키 
이때 총 제작비용을 최소로.
이때 3명이서 1조

인접한 사람끼리의 cost 차이를 저장,
내림차순 정렬 한 이후
K-1인덱스 부터 끝까지의 합을 구함
=> 이유좀 제대로 이해하고 넘어가자.
why? 어차피 인접한 사람들끼리만 모여야 하므로.

K개의 구간을 나눈다면, 경계는 K-1개가 생긴다.
(K 개 묶음이면 양쪽끝을 제외하고 경계는 K-1개가 생긴다.)
그리고 그 K-1개의 경계는 같은조가 아니므로, cost에서 정산되지 않는다!
=> 따라서 cost를 구한 후, 내림차순 정렬하여 K-1개를 제외하는것!

ex)
N = 9  / K = 3 일때
아래와 같이 주어진다면 
1 3 5 6 14 15 19 25 26
 2 2 1 8  1  4  6  1
위와같이 cost 배열이 구해지고, 세 묶음으로 묶으려면 
전체 코스트가 최소가 될 두개의 (3-1) 경계 포인트를 찾아주면 된다.
이때 8, 6이 가장 높은 순으로 두개의 경계점이므로 이를 제외하면 되며,
따라서
(1, 2, 5, 6)  (14, 15, 19)  (25, 26)
이렇게 조를 짜는것이 가장 cost를 최소로 만들어 주는 것임!
"""

N, K = map(int, sys.stdin.readline().split())
# 이미 오름차순 정렬되어 있다.
children = list(map(int, sys.stdin.readline().split()))
# math.ceil() 오름  math.floor() 내림 round() 반올림

answer = 0

costs = [0] * (N-1)
for i in range(0, N-1):
    costs[i] = children[i+1]-children[i]

costs.sort(key=lambda x : -x)
print(sum(costs[K-1:]))