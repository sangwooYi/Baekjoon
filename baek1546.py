import sys
sys.stdin = open("baek1546.txt")


def find_new_avg(n, scores):
    max_score = scores[0]
    for i in range(1, n):
        if max_score <= scores[i]:
            max_score = scores[i]
    res = 0
    for i in range(0, n):
        new = scores[i] / max_score * 100
        res += new
    ans = res / n
    return ans


N = int(input())
SCORES = list(map(int, input().split()))
answer = find_new_avg(N, SCORES)
print(answer)