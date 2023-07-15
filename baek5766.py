import sys
sys.stdin = open("baek5766.txt")


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    chk_map = {}
    for i in range(0, N):
        tmp = list(map(int, input().split()))

        for num in tmp:
            if num in chk_map.keys():
                chk_map[num] += 1
            else:
                chk_map[num] = 1
    
    arr = [0] * len(chk_map.keys())

    idx = 0
    for key in chk_map:
        cnt = chk_map[key]

        arr[idx] = [cnt, key]
        idx += 1
    arr.sort(key=lambda x : (-x[0], x[1]))
    
    # 최고점은 단 한명이라는게 문제 규칙
    second_score = arr[1][0]

    ans = []
    for i in range(1, len(arr)):
        if arr[i][0] < second_score:
            break
        ans.append(arr[i][1])
    print(" ".join(map(str, ans)))