import sys
sys.stdin = open("baek26215.txt")


N = int(input())
arr = list(map(int, input().split()))


ans = 0
arr.sort(reverse=True)

if arr[0] > 1440:
    print(-1)
else:
    while arr[0] > 0:
        if N > 1 and arr[1] > 0:
            arr[1] -= 1
        arr[0] -= 1
        ans += 1
        arr.sort(reverse=True)
        if ans > 1440:
            ans = -1
            break
    print(ans)

