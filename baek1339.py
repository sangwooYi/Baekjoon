import sys
sys.stdin = open("baek1339.txt")


"""
최대 N이 10이고, 각 수의 최대길이 8 반복 많이해 도 크게 상관 X

전략
1. 자릿수가 높으면 더 큰숫자 부여
2. 최대 자릿수가 같은 경우에는 해당 자릿수에서 출연 횟수?
3. 동일 자릿수에서 출연횟수까지 같은경우면 그 다음자리를 체크해야함.
=> 이런 전략으로 우선순위를 정해주는 방법??

딕셔너리 key=알파벳, value는 우선순위용 리스트
ex) 최대 다섯자리이면
[0, 0, 0, 0, 0]
이런 리스트를 선언하고, 각 자리에서 출연한 횟수를 체크
ex [1, 0, 2, 3]
이 결과로 나온 리스트값을 => 숫자로 변환해서 크기 비교 (1023)
이걸로 우선순위 체크 가능!
"""
 
N = int(input())
word = [0] * N
max_len = 0
for i in range(0, N):
    word[i] = list(input())
    if max_len < len(word[i]):
        max_len = len(word[i])


check_dict = {}

for i in range(0, len(word)):
    # 뒤에서부터 해야함!
    for j in range(len(word[i])-1, -1, -1):
        alph = word[i][j]
        index = len(word[i])-1-j
        if alph not in check_dict.keys():
            check_dict[alph] = [0] * max_len
        check_dict[alph][index] += 1

alphs = list(check_dict.keys())
ans_list = [0] * len(alphs)
for i in range(0, len(alphs)):
    temp = check_dict[alphs[i]]
    val = ""
    for j in range(0, len(temp)):
        val = str(temp[j]) + val
    ans_list[i] = [int(val), alphs[i]]
ans_list.sort(key=lambda x : -x[0])

start = 9
for i in range(0, len(ans_list)):
    check_dict[ans_list[i][1]] = start-i

answer = 0
for i in range(0, N):
    po = 0
    for j in range(len(word[i])-1, -1, -1):
        now = word[i][j]
        answer += (check_dict[now] * (10**po))
        po += 1
print(answer)