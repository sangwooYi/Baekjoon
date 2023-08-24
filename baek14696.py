import sys
sys.stdin = open("baek14696.txt")

scores = [0, 1, 10**4, 10**8, 10**12]


N = int(input())
for i in range(0, N):
    a_tmp = list(map(int, input().split()))
    b_tmp = list(map(int, input().split()))

    a_arr = a_tmp[1:]
    b_arr = b_tmp[1:]

    a_score = 0
    b_score = 0

    for i in range(0, len(a_arr)):
        a_score += scores[a_arr[i]]

    for i in range(0, len(b_arr)):
        b_score += scores[b_arr[i]]

    if a_score > b_score:
        print("A")
    elif a_score < b_score:
        print("B")
    else:
        print("D")