import sys
sys.stdin = open("baek14369.txt")

"""
1차로 z => zero / w => two  / u => four / x => six/ g => eight 를 체크하여 제외
(0, 2, 4, 6, 8 제외)
2차로 s => seven / f => five / t => three
3차로 i => nine / o => one

항상 유일한 답이 보장되는 문제이므로
이렇게 접근 가능한것!
"""

# 숫자에 해당하는 알파벳 체크용 dict 생성
def make_cur_dict(cur_str):

    tmp_dict = {}
    for i in range(0, len(cur_str)):
        if cur_str[i] in tmp_dict.keys():
            tmp_dict[cur_str[i]] += 1
        else:
            tmp_dict[cur_str[i]] = 1
    return tmp_dict

# 문자열 체크
def chk_str(encode_str, tmp_dict, visited):

    for i in range(0, len(encode_str)):
        if visited[i]:
            continue
        if encode_str[i] in tmp_dict.keys():
            if tmp_dict[encode_str[i]] > 0:
                visited[i] = True
                tmp_dict[encode_str[i]] -= 1    


def decode_number(encode_str):
    
    conv_dict = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, 
                 "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}
    visited = [False] * len(encode_str)
    res_arr = []
    chk_num = 0

    # 1차로 z => zero / w => two  / u => four / x => six / g => eight 를 체크하여 제외
    while chk_num < len(encode_str):
        # 초기화
        cur_flag = ""
        for i in range(0, len(encode_str)):
            if visited[i]:
                continue
            if encode_str[i] == "Z":
                cur_flag = "ZERO"
                break
            if encode_str[i] == "W":
                cur_flag = "TWO"
                break
            if encode_str[i] == "U":
                cur_flag = "FOUR"
                break
            if encode_str[i] == "X":
                cur_flag = "SIX"
                break
            if encode_str[i] == "G":
                cur_flag = "EIGHT"
                break
        # 이젠 없음
        if len(cur_flag) == 0:
            break
        # 해당 문자열 체크
        chk_num += len(cur_flag)
        chk_dict = make_cur_dict(cur_flag)
        chk_str(encode_str, chk_dict, visited)
        res_arr.append(conv_dict[cur_flag])
    
    # 2차로 s => seven / f => five / t => three
    while chk_num < len(encode_str):
        
        cur_flag = ""
        for i in range(0, len(encode_str)):
            if visited[i]:
                continue
            if encode_str[i] == "S":
                cur_flag = "SEVEN"
                break
            if encode_str[i] == "F":
                cur_flag = "FIVE"
                break
            if encode_str[i] == "T":
                cur_flag = "THREE"
                break
        if len(cur_flag) == 0:
            break
        # 해당 문자열 체크
        chk_num += len(cur_flag)
        chk_dict = make_cur_dict(cur_flag)
        chk_str(encode_str, chk_dict, visited)
        res_arr.append(conv_dict[cur_flag])        

    # 3차로 i => nine / o => one
    while chk_num < len(encode_str):

        cur_flag = ""
        for i in range(0, len(encode_str)):
            if visited[i]:
                continue
            if encode_str[i] == "I":
                cur_flag = "NINE"
                break
            if encode_str[i] == "O":
                cur_flag = "ONE"
                break
        if len(cur_flag) == 0:
            break
        # 해당 문자열 체크
        chk_num += len(cur_flag)
        chk_dict = make_cur_dict(cur_flag)
        chk_str(encode_str, chk_dict, visited)
        res_arr.append(conv_dict[cur_flag])        
    return res_arr

T = int(input())
for tc in range(1, T+1):

    encode_str = input()
    result =decode_number(encode_str)
    # 오름차순
    result.sort()
    answer = "".join(map(str, result))
    print(f"Case #{tc}: {answer}")