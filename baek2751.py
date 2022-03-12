import sys
sys.stdin = open("baek2751.txt")

N = int(sys.stdin.readline())


# def swap(arr, idx1, idx2):
#     temp = arr[idx1]
#     arr[idx1] = arr[idx2]
#     arr[idx2] = temp


# def quickSort(arr, left, right):
#     pl = left
#     pr = right
#     pv = arr[(pl + pr) // 2]
#     while pl <= pr:
#         while arr[pl] < pv:
#             pl += 1
#         while arr[pr] > pv:
#             pr -= 1
#         # 아직 범위가 유효할때만
#         if (pl <= pr):
#             # 바꾸고나서 한번 더이 동
#             swap(arr, pl, pr)
#             pl += 1
#             pr -= 1
#     # 위에서 while문 벗어났으면 이미 pl > pr 인 상황
#     if left < pr:
#         quickSort(arr, left, pr)
#     if pl < right:
#         quickSort(arr, pl, right)

INP = [0] * 1000000
idx = 0
for i in range(0, N):
    now = int(sys.stdin.readline())
    INP[idx] = now
    idx += 1


NUMS = INP[0:idx]
NUMS.sort()
for i in range(0, N):
    print(NUMS[i])
