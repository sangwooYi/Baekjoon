import sys
sys.stdin = open("baek1270.txt")

N = int(sys.stdin.readline())
for tc in range(0, N):
    tmp = list(map(int, sys.stdin.readline().split()))
    total_cnt = tmp[0]
    nums = tmp[1:]

    count_dict = {}

    for num in nums:
        if num in count_dict.keys():
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # dict의 길이는 결국 key의 갯수와 같음
    res_arr = [0] * len(count_dict)
    idx = 0
    for key in count_dict:
        res_arr[idx] = [key, count_dict[key]]
        idx += 1
    res_arr.sort(key=lambda x : -x[1])

    max_num, max_cnt = res_arr[0]
    if max_cnt > (total_cnt//2):
        print(max_num)
    else:
        print("SYJKGW")