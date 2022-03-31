from operator import is_
import sys
sys.stdin = open("baek5052.txt")
"""
특정 번호가
다른 번호에 포함관계가 발생하는지를 체크해야하는 문제
길어야 10자리이므로, 일일이 비교 가능할지도?


아이디어1.
입력 받은뒤에, 글자수 별로 정렬하고,
작은 글자 => 많은글자순으로 for문돌리며 포함관계 체크
전화번호가 같은경우는 없으므로, 같은 글자수끼리 비교할 필요는 X

정석적인 풀이는 아래와같이 key-value 를 이용하는것
근데 내가 푼풀이도 아래와 같은 로직인것!

def solution(phone_book):
    temp_dict = {}
    for idx in range(0, len(phone_book)):
        # key는 해당 인덱스의 값, value는 해당 값의 인덱스
        temp_dict[phone_book[idx]] = idx
    # 해당 번호값의 일부 중 딕셔너리에 저장된 값이 있는지를 전부체크
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book[i])):
            # dict에서 key값 체크할때는 .keys() 를 붙이는게 효율적이다!
            그냥 in dict라고 서도 key값이 있는지를 체크해주기는 함!
            if (phone_book[i][:j] in temp_dict.keys()):
                return False
    return True

"""


# 이게 아래로 짤때보타 2초나 더 적게걸린다 ㄷㄷ
# key-value로 푸는 풀이 익숙해질것!
def solution(phone_book):
    check_dict = {}
    for idx in range(0, len(phone_book)):
        # 여기서 value값은 사실상 의미 없다. 그냥 저장하는것
        check_dict[phone_book[idx]] = idx
    for i in range(0, len(phone_book)):
        # 각 전화번호부 각각을 빼서, 자기의 번호중의 일부가
        # 다른 번호에 속해있는것이 없는지를 체크하는것, dict에서 key값이 있냐없냐만 체크하면 된다!
        # 시간복잡도는 최대 10 * 1만 == 10만회 연산하는것!
        for j in range(0, len(phone_book[i])):
            if (phone_book[i][:j] in check_dict.keys()):
                return "NO"
    return "YES"

T = int(input())
for tc in range(0, T):
    N = int(input())
    P = [0] * N
    for i in range(0, N):
        P[i] = input()
    ans = solution(P)
    print(ans)


# 아래풀이도 가능은하나, 위의 풀이에 비해 비효율적
# T = int(input())
# for tc in range(0, T):
#     N = int(input())
#     # 1자리부터 10자리까지
#     check = [[] for _ in range(0, 11)]
#     min_len = 10
#     max_len = 0
#     for i in range(0, N):
#         tel = input()
#         check[len(tel)].append(tel)
#         if min_len >= len(tel):
#             min_len = len(tel)
#         if max_len <= len(tel):
#             max_len = len(tel)
#     # max_len-1 까지만 순회하면 된다.
#     is_consist = True
#     for i in range(min_len, max_len):
#         if not is_consist:
#             break
#         if check[i]:
#             for j in range(0, len(check[i])):
#                 if not is_consist:
#                     break
#                 # 이 전화번호가 다른데에 포함관계가 없는지 체크해야함
#                 temp = check[i][j]
#                 for k in range(i+1, max_len+1):
#                     if not is_consist:
#                         break
#                     # 있는 경우만
#                     if check[k]:
#                         for h in range(0, len(check[k])):
#                             now = check[k][h]
#                             # 하나라도 속하면 그냥 끝내면 됨
#                             flag = True
#                             # i자리까지만 체크하면 된다.
#                             for p in range(0, i):
#                                 if temp[p] != now[p]:
#                                     flag = False
#                                     break
#                             if flag:
#                                 is_consist = False
#                                 break
#     if is_consist:
#         print("YES")
#     else:
#         print("NO")                        
