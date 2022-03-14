import sys
sys.stdin = open("baek10816.txt")

"""
전형적으로 리스트 - 딕셔너리 같이 사용하는 문제
"""

def count_cards(n, cards, m, finds):
    cards_dict = {}   
    result = [0] * m
    # 
    for i in range(0, n):
        if cards[i] in cards_dict.keys():
            cards_dict[cards[i]] += 1
        else:
            cards_dict[cards[i]] = 1
    for i in range(0, m):
        now = finds[i]
        # cards_dict의 key값으로 있는애면 해당 value값 저장
        if now in cards_dict.keys():
            result[i] = cards_dict[now]
        # 아니면 0 저장 , 없는것
        else:
            result[i] = 0

    return result


    # return result

N = int(input())
CARDS = list(map(int, input().split()))
M = int(input())
FINDS = list(map(int, input().split()))

answer = count_cards(N, CARDS, M, FINDS)
for i in range(0, M):
    if i == M-1:
        print(answer[i])
    else:
        print(answer[i], end=" ")