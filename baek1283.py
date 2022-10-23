import sys
sys.stdin = open("baek1283.txt")

"""
아스키 코드 기준
대문자+32 == 소문자
chr(아스키코드) => 알파벳으로 변환됨
ord(숫자) => 아스키코드로 변환됨
A = 65   Z = 90 
a = 97   z = 122

1. 일단 각 단어들의 첫글자중 남는게 있으면 그게 단축키
2. 1번조건이 안되면 왼쪽부터 차례대로 순회해서 그 중 걸리는게 단축키
3. 1, 2 둘다안되면 그냥 pass 단, 대/소문자 구분 안함
"""

def is_capital(alph):
    # 65 ~ 90까지가 대문자
    if 65 <= ord(alph) <= 90:
        return True
    return False

def conv_to_capital(alph):
    # 만약 소문자 범위 아니면 다 무시
    if 97 <= ord(alph) <= 122:
        return chr(ord(alph)-32)
    return alph

    

N = int(input())
elements = [0] * N
for i in range(0, N):
    elements[i] = input().split()

check_dict = {}

for element in elements:
    # 첫글자 체크
    flag = False
    for i in range(0, len(element)):
        word = element[i]
        first_letter = word[0]
        # 무조건 check_dict key값은 대문자로
        if not is_capital(first_letter):
            # 소문자인 경우 일단 체크용은 대문자로 변경
            first_letter = conv_to_capital(first_letter)
        # 1번 조건에 해당되는 경우
        if first_letter not in check_dict.keys():
            check_dict[first_letter] = 1
            word = f"[{word[0]}]{word[1:]}" 
            element[i] = word
            flag = True
            break
    # 1번조건은 안되는 경우, 왼쪽부터 차례대로 탐색
    if not flag:
        for i in range(0, len(element)):
            if flag:
                break
            word = element[i]
            # 각 단어의 첫글자는 이미 체크함
            for j in range(1, len(word)):
                now_letter = word[j]
                if not is_capital(now_letter):
                    now_letter = conv_to_capital(now_letter)

                if now_letter not in check_dict.keys():
                    check_dict[now_letter] = 1
                    tmp = ""
                    for k in range(0, len(word)):
                        if k == j:
                            tmp += f"[{word[k]}]"
                        else:
                            tmp += word[k]
                    element[i] = tmp
                    flag = True
                    break

for element in elements:
    print(" ".join(element))