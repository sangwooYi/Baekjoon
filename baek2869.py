import sys
sys.stdin = open("baek2869.txt")

"""
요지는 매일밤 미끄러진다는거!
따라서 미끄러지기전에 도달했을때를 성공 날짜로 계산한다는게 포인트

(a - b) * (days) + a >= goal 일때 인순간을 찾는것

(a - b) * days >= goal - a
return a 

항상 v >= a > b >= 1

"""

def count_require_days(a, b, goal):
    # 예외 처리
    if a >= goal:
        return 1
    # goal > a 
    days = (goal - a) // (a - b)
    # 나머지가 있으면 올림처리 해주어야함! 이게 핵심
    res = (goal - a) % (a - b)
    if res:
        days += 1
    return days + 1

A, B, V = map(int, input().split())
answer = count_require_days(A, B, V)
print(answer)