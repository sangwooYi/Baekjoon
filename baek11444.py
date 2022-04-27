"""
메모이제이션 방법 외에도,
피보나치를 아래처럼 
행렬로도 풀 수 있다. 이부분 꼭 학습해 둘 것

Fn+1 Fn     1  1 ^n
Fn   Fn-1 = 1  0

근데 이게 더 문제풀기 편한듯
Fn+2    1  1 *n  1
Fn+1  = 1  0     0


다시한번 말하지만
(a + b) mod N = ((a mod N) + (b mod N)) mod N
(a - b) mod N = ((a mod N) - (b mod N)) mod N
(a * b) mod N =  (a mod N)  * (b mod N) mod N
이로인해 분할정복이 가능!

"""  
p = 1000000007

def power(adj, n):
    if n == 1:
        return adj
    elif n % 2:
        # 홀수 승이면 ()*n-1 * adj 
        return multi(power(adj, n-1), adj)
    else:
        # 짝수승이면 ()**(n//2) * ()**(n//2)
        return power(multi(adj, adj), n//2)

# 행렬 곱셈 할 줄 알아야 한다.
def multi(a, b):
    # N*M 행렬과  M*X 행렬의 곱의 결과 행렬 사이즈는 (N*X) 행렬
    temp = [[0] * len(b[0]) for _ in range(0, 2)]
    for i in range(0, 2):
        for j in range(0, len(b[0])):
            sum = 0
            for k in range(0, 2):
                sum += a[i][k] * b[k][j]
            # 모듈러 연산으로 인해 이런풀이가 가능!
            temp[i][j] = sum % p
    return temp
    
N = int(input())
adj = [[1, 1], [1, 0]]

start = [[1], [1]]
if N < 3:
    ans = 1
else:
    # N==3 일때, [[1, 1],[1, 0]] *[[1], [0]] == [[1], [1]]
    ans = multi(power(adj, N-2), start)[0][0]
print(ans) 