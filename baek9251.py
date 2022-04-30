import sys
sys.stdin = open("baek9251.txt")

"""
LCS알고리즘도 익혀두자. 다이나믹 프로그래밍의 일종
이것도 DP의 일종이라고 합니다! 꼭 익혀두자.
참고 안하고 혼자서 풀 수도 있어야한다!

DP[i][j] (앞의 수열 i번째 / 뒤의수열 j 번째까지 최장수열 길이에 해당하는 값)
만약 앞[i] == 뒤[j] 이면  DP[i][j] = DP[i-1][j-1] + 1 (수열이 연속되어야하므로!)
     앞[i-1] != 뒤[j-1] 이면 max(DP[i-1][j], DP[i][j-1])
""" 

A = input()
B = input()

# 0행 / 0열은 마진으로 둔다.
DP = [[0] * (len(B)+1) for _ in range(0, len(A)+1)]

for i in range(0, len(A)):
    for j in range(0, len(B)):
        # 같으면!
        if A[i] == B[j]:
            DP[i+1][j+1] = DP[i][j] + 1
        # 다르면!
        else:
            DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])
print(DP[len(A)][len(B)])

