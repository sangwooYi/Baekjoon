import sys
sys.stdin = open("baek1157.txt")

"""
a ~ z 는 97 ~ 122 (26자)
A ~ Z 는 65 ~ 90

아스키 코드기준으로 소문자 - 32 를 하면 대문자가 나온다!

리스트를 이용! 
소문자 => 32를 빼서 대문자로 바꿔주고
대문자 기준 65를 빼서 인덱스로 치환하여 저장 
"""

INP =list(input())
count = [0] * 26 
for i in range(0, len(INP)):
    alph = ord(INP[i])
    if 97 <= alph <= 122:
        idx = (alph - 97)
    else:
        idx = (alph - 65)
    count[idx] += 1
ans = [0]
max_count = count[0]
for i in range(1, len(count)):
    if count[i] > max_count:
        ans = [i]
        max_count = count[i]
    elif count[i] == max_count:
        ans.append(i)
if len(ans) > 1:
    print("?")
else:
    print(chr(ans[0]+65))