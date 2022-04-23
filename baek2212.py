import sys
sys.stdin = open("baek2212.txt")

"""
이 아이디어로 푸는 문제는 앞으로 무조건 맞춰야한다.

각 노드간의 거리차이를 arr로 계산한 후
K 개의 기지국을 세운다는건
K 영역으로 쪼갤 수 있다는것,
따라서 거리차이 arr를 sort한 후, 
큰 순서대로 (K-1) 개만큼을 제외한다.
나머지의 sum이 정답. (K개의 영역으로 쪼개는것)
ex)
3 6 7 8 10 12 14 15 18 20
 3 1 1 2  2  2  1  3  2
따라서
3 / 6 7 8 / 10 12 / 14 15 / 18 20
0    1 1      2       1       2
각 쪼개진 영역에서는 어떻게 기지국을 설치하던간에,
위에서 계산한 거리차이 arr값이 된다.
이 아이디어는 꼭 기억하자!
"""

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

answer = 0
# N <= K 이면 그냥 모든 노드에 설치 가능 따라서 0
if N > K:
    gap = [0]*(N-1)
    idx = 0
    for i in range(0, N-1):
        gap[idx] = sensors[i+1]-sensors[i]
        idx += 1
    gap.sort()
    for i in range(0, len(gap)-K+1):
        answer += gap[i]
print(answer)
