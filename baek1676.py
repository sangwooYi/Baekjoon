# import sys
# sys.stdin = open("baek1676.txt")


def factorial(n):
    if n <= 1:
        return 1
    DP = [1, 1]
    for i in range(2, n+1):
        DP.append(DP[i-1] * i)
    return DP[n]


N = int(input())
facto_res = str(factorial(N))
ans = 0
for i in range(len(facto_res)-1, -1, -1):
    if facto_res[i] == "0":
        ans += 1
    else:
        break
print(ans)





