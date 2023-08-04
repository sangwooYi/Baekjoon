arr = list(map(int, input().split()))

def swap(arr, idx1, idx2):
    tmp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = tmp

ans = [1, 2, 3, 4, 5]


while arr != ans:

    for i in range(0, 4):
        if arr[i] > arr[i+1]:
            swap(arr, i, i+1)
            print(" ".join(map(str, arr)))
