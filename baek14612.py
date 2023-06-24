import sys
sys.stdin = open("baek14612.txt")


def print_arr():
    if len(arr) == 0:
        print("sleep")
    else:
        for i in range(0, len(arr)):
            if i < len(arr)-1:
                print(arr[i][0], end=" ")
            else:
                print(arr[i][0])

N, M = map(int, input().split())
arr = []
for i in range(0, N):
    tmp = list(input().split())

    oper = tmp[0]
    if oper == "order":
        t_num, req_time = tmp[1:]

        arr.append([int(t_num), int(req_time)])

    elif oper == "complete":
        t_num = tmp[1]

        tmp_arr = []
        for j in range(0, len(arr)):
            if arr[j][0] != int(t_num):
                tmp_arr.append(arr[j])
        arr = tmp_arr
    # sort
    else:
        arr.sort(key=lambda x : (x[1], x[0]))
    print_arr()