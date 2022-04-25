import sys
sys.stdin = open("baek15657.txt")
"""
순열/조합외에도
이것처럼 비내림차순 순열같은걸 응용해서 만들수도 있어야 한다!

"""



def comb(arr, out, start, depth, n, r):
    if r == 0:
        for i in range(0, len(out)):
            if i == len(out) - 1:
                print(out[i])
            else:
                print(out[i], end=" ")
        return
    for i in range(start, len(arr)):
        out[depth] = arr[i]
        comb(arr, out, i, depth+1, n, r-1)



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
check = [0] * M
comb(nums, check, 0, 0, N, M)