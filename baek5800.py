import sys
sys.stdin = open("baek5800.txt")

T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    scores = tmp[1:]
    num = tmp[0]

    scores.sort()
    
    max_score = scores[0]
    min_score = scores[0]
    max_gap = 0
    now = scores[0]

    for i in range(1, num):
        cur_score = scores[i]
        cur_gap = scores[i]-scores[i-1]
        max_score = max(max_score, cur_score)
        min_score = min(min_score, cur_score)
        max_gap = max(max_gap, cur_gap)

    print(f"Class {tc}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {max_gap}")