import sys
import heapq
sys.stdin = open("baek23559.txt")


"""
1000원짜리 메뉴부터 다 먹고나서
5000원짜리 메뉴로 선택 가능하면서, 더 가치가 큰 경우를 최대한 체크

그리고 중요한건 못 먹는 날은 없다!
(따라서 5000원 메뉴를 골라서 다른날 4일동안 못먹거나 이런 경우는 없다!)

백준에서 제시하는 문제풀이유형에 너무 집착하지 말자..
"""

N, K = map(int, sys.stdin.readline().split())
menus_info = [0] * N
for i in range(0, N):
    a_taste, b_taste = map(int, sys.stdin.readline().split())
    menus_info[i] = [a_taste, b_taste]

menus_info.sort(key = lambda x : (-(x[0]-x[1])))

answer = 0
res_money = K
for i in range(0, N):
    answer += menus_info[i][1]
    res_money -= 1000

for i in range(0, N):
    if res_money < 4000:
        break
    if menus_info[i][0] > menus_info[i][1]:
        res_money -= 4000
        answer += (menus_info[i][0]-menus_info[i][1])
print(answer)
