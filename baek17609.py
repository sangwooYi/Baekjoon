import sys
sys.stdin = open("baek17609.txt")
"""
어디를 pass할건지 정하는 부분에 반례가 나온다!
baaba
이런 반례를 혼자서 찾아낼 수 있어야 한다!
"""

# 무조건 회문인지 체크하는 친구
def is_palindrome(arr):
    for i in range(0, len(arr)):
        if arr[i] != arr[len(arr)-1-i]:
            return False
    return True


def check_palindrome(arr):
    flag = True
    pl = 0
    pr = len(arr) - 1
    while pl < pr:
        if arr[pl] != arr[pr]:
            # 이미 기회를 쓴상태면 회문이 아님
            if not flag:
                return 2
            # 유사회문인지 체크
            # pl+1 ~ pr
            temp1 = arr[pl+1:pr+1]
            # pl ~ pr-1
            temp2 = arr[pl:pr]
            # 어디를 pass해야 회문이 되는지 체크해야 한다.
            if is_palindrome(temp1):
                flag = False
                pl += 1
            elif is_palindrome(temp2):
                flag = False
                pr -= 1
            # 유사회문도 아닌경우
            else:
                return 2
        else:
            pl += 1
            pr -= 1
    if flag:
        return 0
    return 1

T = int(input())
for i in range(0, T):
    sentence = list(input())
    ans = check_palindrome(sentence)
    print(ans)