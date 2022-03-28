import sys
sys.stdin = open("baek8958.txt")

N = int(input())
for i in range(0, N):
    quiz = list(input())
    total = 0
    score = 0
    for j in range(0, len(quiz)):
        if quiz[j] == "O":
            score += 1
            total += score
        elif quiz[j] == "X":
            score = 0
    print(total)