import sys
sys.stdin = open("baek1541.txt")
"""
최솟값을 찾는 문제이므로

파싱을 -기준으로 하자..
좀 쉽게 생각합시다 ..

이문제는 꼭 다시 풀어보자! 파싱 연습 문제
뭉탱이로 묶어야 할때는 고민하지말고 활용하면 된다!
"""


inp_eq = list(input().split("-"))
part = []
for i in range(0, len(inp_eq)):
    tmp = list(map(int, inp_eq[i].split("+")))
    tmp_sum = 0
    for j in range(0, len(tmp)):
        tmp_sum += tmp[j]
    part.append(tmp_sum)
answer = part[0]
for i in range(1, len(part)):
    answer -= part[i]
print(answer)