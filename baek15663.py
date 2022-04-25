import sys
sys.stdin = open("baek15663.txt")


def permutation(arr, out_arr, visited, depth, n, r):
    if depth == r:
        if tuple(out_arr) not in res_dict.keys():
            # 어차피 value 쓸데 없음
            res_dict[tuple(out_arr)] = 1
            for i in range(0, len(out_arr)):
                if i == len(out_arr)-1:
                    print(out_arr[i])
                else:
                    print(out_arr[i], end=" ")
        return
    for i in range(0, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        out_arr[depth] = arr[i]
        permutation(arr, out_arr, visited, depth+1, n, r)
        visited[i] = False

N, M = map(int, input().split())
num = list(map(int, input().split()))
temp = [0] * M
# 중복방지
res_dict = {}
check = [False] * N
num.sort()
permutation(num, temp, check, 0, N, M)
