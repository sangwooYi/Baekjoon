import sys
sys.stdin = open("baek2822.txt")

scores = [0] * 8

for idx in range(0, 8):
    score = int(input())
    scores[idx] = [score, idx+1]
scores.sort(key=lambda x : -x[0])

total_score = 0
idx_arr = [0] * 5
for i in range(0, 5):
    total_score += scores[i][0]
    idx_arr[i] = scores[i][1]
idx_arr.sort()
print(total_score)
print(" ".join(map(str, idx_arr)))

