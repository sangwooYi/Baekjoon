"""
이걸 어케맞추냐 ..ㅡㅡ?
"""
import math

star = ['  *   ', ' * *  ', '***** ']

def make_star(shift):
    c = len(star)
    for i in range(0, c):
        # 삼각형을 하나더 만들고
        star.append(star[i] + star[i])
        # 그 전의 만들어 놓았던 삼각형은 shift * (3*space)만큼 민다
        star[i] = ("   "*shift + star[i] + "   "*shift)

N = int(input())
# math.log(A, b) 는 logbA 를 구하는 것! N = 3*2**k 였으므로 log2(2**k)== k == N///3
K = int(math.log(int(N/3), 2))
for i in range(0, K):
    make_star(int(pow(2, i)))
for i in range(0, N):
    print(star[i])