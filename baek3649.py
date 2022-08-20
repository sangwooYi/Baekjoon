import sys
sys.stdin = open("baek3649.txt")


while True:
    X = sys.stdin.readline()
    if len(X) == 0:
        break
    X = int(X)
    target = X * 10000000
    N = int(sys.stdin.readline())
    blocks = [0] * N
    for i in range(0, N):
        blocks[i] = int(sys.stdin.readline())
    blocks.sort()
    left = 0
    right = N-1

    while left <= right:
        now = blocks[left] + blocks[right]
        if now > target:
            right -= 1
        elif now < target:
            left += 1
        else:
            break
    if left >= right:
        print("danger")
    else:
        print(f"yes {blocks[left]} {blocks[right]}")