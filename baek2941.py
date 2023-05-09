word = input()

answer = 0
flag_cnt = 0
for i in range(0, len(word)):
    if flag_cnt:
        flag_cnt -= 1
        continue
    answer += 1
    # 가장 마지막단어면 따질 필요도 없음
    if i < len(word)-1:
        if word[i] == "c":
            if word[i+1] == "=" or word[i+1] == "-":
                flag_cnt = 1
        if word[i] == "d":
            if word[i+1] == "-":
                flag_cnt = 1
            if i < len(word)-2 and word[i+1] == "z" and word[i+2] == "=":
                flag_cnt =  2
        if word[i] == "l" and  word[i+1] == "j":
            flag_cnt = 1
        if word[i] == "n" and word[i+1] == "j":
            flag_cnt = 1
        if word[i] == "s" and word[i+1] == "=":
            flag_cnt = 1
        if word[i] == "z" and word[i+1] == "=":
            flag_cnt = 1
print(answer)


# 그냥 replace 쓰면 됨..
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    # 파이썬 replace는 기본적으로 replaceAll임 (count = -1 이 디폴트, 이건 전체 변경)
    # 만약 변경 횟수를 정하고 싶으면 .replace(찾는문자, 대체할문자, count=3 (이러면 최대 3회 변경)) 이런식으로
    # count 인자를 추가로 설정해주면 된다
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))