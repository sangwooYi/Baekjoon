import sys
sys.stdin = open("baek5671.txt")


while True:
    # 종료조건 없을때
    # input()은 입력없으면 에러나지만
    # sys.stdin.readline() 은 우선 입력값 없어도 작동은 한다!
    tmp = sys.stdin.readline()
    if not tmp:
        break
    tmp = tmp.rstrip()
    M, N = map(int, tmp.split())
    
    cnt = 0
    for num in range(M, N+1):
        tmp_map = {}

        num_s = str(num)
        flag = False
        for i in range(0, len(num_s)):
            if num_s[i] in tmp_map.keys():
                flag = True
                break
            tmp_map[num_s[i]] = 1
        if not flag:
            cnt += 1
    print(cnt)