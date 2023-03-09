import sys
sys.stdin = open("baek2529.txt")


def perm(in_arr, out_arr, visited, depth, n, r):
    global max_res
    global min_res
    if depth == r:
        tmp = ''
        for i in range(0, r):
            tmp += str(out_arr[i])
        conv_int = int(tmp)
        if int(max_res) < conv_int:
            max_res = tmp
        if int(min_res) > conv_int:
            min_res = tmp
        return
    for i in range(0, n):
        if visited[i]:
            continue
        if depth > 0:
            sign = inequality_signs[depth-1]
            
            if sign == ">":
                if out_arr[depth-1] <= in_arr[i]:
                    continue
            else:
                if out_arr[depth-1] >= in_arr[i]:
                    continue
        visited[i] = True
        out_arr[depth] = in_arr[i]
        perm(in_arr, out_arr, visited, depth+1, n, r)
        visited[i] = False


K = int(input())
inequality_signs = list(input().split())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visited = [False] * 10
out_arr = [0] * (K+1)

min_res = 987654321987
max_res = 0
perm(nums, out_arr, visited, 0, 10, K+1)

print(max_res)
print(min_res)