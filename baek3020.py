import sys
sys.stdin = open("baek3020.txt")

"""
백준 풀이 힌트에 너무 의존하지말자..
누적합으로 푸는게 훨씬 적합한 문제!!

누적합은
석순배열    seok[i]   
종유석배열  jong[i]
초깃 input 받으면서ㅜ i높이인 갯수를 체크 해당배열++ 
=> 그 이후에 높이 H-1 ~ 1까지 순회하면서ㅏ
seok[h] += seok[h+1]
jong[h] += jong[h+1]
=> 즉 높이 h일때 걸리는 석순 / 종유석의 수를 체크하는것
""" 

# 누적합
N, H = map(int, sys.stdin.readline().split())

seok = [0] * (H+1)
jong = [0] * (H+1)

for i in range(0, N):
    cur_h = int(sys.stdin.readline().rstrip())
    if (i%2):
        jong[cur_h] += 1
    else:
        seok[cur_h] += 1

for h in range(H-1, 0, -1):
    jong[h] += jong[h+1]
    seok[h] += seok[h+1]

min_break = N+100
min_cnt = 1
for h in range(1, H+1):

    cur_break = seok[h] + jong[H+1-h]
    if cur_break < min_break:
        min_break = cur_break
        min_cnt = 1
    elif cur_break == min_break:
        min_cnt += 1
print(f"{min_break} {min_cnt}")
