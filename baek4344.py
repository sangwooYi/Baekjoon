import sys
sys.stdin = open("baek4344.txt")

T = int(input())
for tc in range(0, T):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    nums = tmp[1:]
    
    total = 0
    for i in range(0, n):
        total += nums[i]
    average = total/n

    cnt = 0
    for i in range(0, n):
        if nums[i] > average:
            cnt += 1
    
    # n번쨰 자리 반올림
    res = round((cnt/n)*100, 3)

    # 소숫점 formating 하는법 자바 system.printf 유사함 .nf 에서 n으로 소숫점출력자릿수 결정
    print(f"{res:.3f}%")
