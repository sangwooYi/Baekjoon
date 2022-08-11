
import sys
sys.stdin = open("baek3663.txt")

"""
최대 반복횟수가 100 * 1000 * 26
따라서 기껏해야 약 200 ~ 300만회 연산임 (충분히 시간적으로 여유)

각 알파벳마다 필요 횟수 표는 아래와 같다.
a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
                            -16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4- 3 -2 -1
즉 n까지는 1씩증가
o부터는1 씩감소

이제 횡방향으로 최소횟수를 구해야 한다. 
=> A 가 어떻게 배치되어있는가에 따라 달라짐 (얘는 전ㅇ혀 동작안해도 되는 애이므로)
=> 생각을 조금만 더 해 보자.. 충분히 혼자서 풀 수 있는 문제였는데
"""


T = int(input())

# 각 알파벳마다 필요한 동작 횟수
req_time_made_chr = {}
start = ord("A")
time = 0
for i in range(0, 26):
    req_time_made_chr[chr(start+i)] = time
    if i < 13:
        time += 1
    else:
        time -= 1



for tc in range(0, T):
    answer = 0
    chars = list(input())
    size = len(chars)

    for i in range(size-1, -1, -1):
        answer += req_time_made_chr[chars[i]]

    move = size-1
    # 이부분 이해하자.
    for idx, char in enumerate(chars):
        next_idx = idx + 1
        next_i = idx+1
        
        while next_i < size and chars[next_i] == 'A':
            next_i += 1
        # -> 후 <-  / <- 후 -> 를 비교
        # idx는 그냥 시작점 next_i 는 idx+1 이후부터 A가 안나오는 첫지점
        move = min(move, 2*idx + size - next_i, 2*(size-next_i) + idx)
    answer += move
    print(answer)
