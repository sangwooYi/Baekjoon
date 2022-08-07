import sys
sys.stdin = open("baek1958.txt")


"""
각 문자열 최대길이 100
따라서 O(N**3)도 충분히 가능 
"""

A = list(input())
B = list(input())
C = list(input())

DP = [[[0] * (len(C)+1) for _ in range(0, len(B)+1)] for _ in range(0, len(A)+1)]

for i in range(0, len(A)):
    for j in range(0, len(B)):
        for k in range(0, len(C)):
            if A[i] == B[j] == C[k]:
                DP[i+1][j+1][k+1] = DP[i][j][k] + 1
            else:
                DP[i+1][j+1][k+1] = max(DP[i][j+1][k+1], DP[i+1][j][k+1], DP[i+1][j+1][k])
print(DP[len(A)][len(B)][len(C)])