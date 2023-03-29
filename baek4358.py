import sys
sys.stdin = open("baek4358.txt")


check_dict = {}

total_cnt = 0
while True:
    now = sys.stdin.readline().rstrip()
    if len(now) == 0:
        break
    total_cnt += 1
    if now in check_dict.keys():
        check_dict[now] += 1
    else:
        check_dict[now] = 1

dict_keys = list(check_dict.keys())
dict_keys.sort()

for key in dict_keys:
    cnt = check_dict[key]

    # round(값, n) 값을 n번쨰자리에서 반올림
    rate = round((cnt/total_cnt)*100, 4)
    # f스트링 쓸때 printf 처럼 소숫점 자릿수지정도 가능하다!
    print(f"{key} {rate:.4f}")