import sys
sys.stdin = open("baek10830.txt")

"""
행렬 곱셈
N*M 행렬 * M*L행렬 == (N*L 행렬) !

분할 정복을 통한 제곱으로 푼다!
행렬 곱셈 익혀두자! + 분할정복으로 곱하는 방법까지
(이건 피보나치로 방법중 하나로도 이어짐! )
()*N 에서 N이 홀수 => ()*N-1 * ()
짝수 => ()*N//2  * ()*N//2

+ 분할정복에서는
mod 연산이 필수!
(a±b) mod N = ((a mod N) ± (b mod N)) mod N
(a*b) mod N = ((a mod N) * (b mod N)) mod N
나누기도 성립!

반례 주의! 거듭제곱 1승일때
기존의 내 방법은 나머지 처리를 못한다!
1000 1000
1000 1000 이게 바로 반례!
반례 찾는 tip: 보통 일반적으로 boundary 값/문제 조건에 있다!
(ex) 1 ~ 1000 까지 조건이라면 1일때 / 1000일때 답이 잘나오는지 체크)

반례 찾을때 제발 바로 검색하려고 하지말자.. 습관 잘 들여야하!
"""

# 행렬 ** n 승
def power(mat, n):
    if n == 1:
        return mat
    
    elif n % 2:
        return multi(power(mat, n-1), mat)
    
    else:
        return power(multi(mat, mat), n//2)

# 행렬 곱  (A*B) (B*C) 행렬끼리 곱하면 (A*C) 행렬이 됨
def multi(a, b):
    adj = [[0] * len(b[0]) for _ in range(0, len(a))]
    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            sum = 0
            for k in range(0, len(b)):
                sum += a[i][k] * b[k][j] 
            # mod 연산으로 인해 이렇게 해도 된다.
            adj[i][j] = sum % 1000
    return adj

N, B = map(int, input().split())
MATRIX = [0] * N
for i in range(0, N):
    MATRIX[i] = list(map(int, input().split()))

ans = power(MATRIX, B)
for row in range(0, len(ans)):
    for col in range(0, len(ans[0])):
        if col == len(ans[0]) - 1:
            print(ans[row][col] % 1000)
        else:
            print(ans[row][col] % 1000, end=" ")