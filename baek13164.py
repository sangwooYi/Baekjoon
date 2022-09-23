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