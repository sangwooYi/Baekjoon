"""
기껐해야 N이 100만까지이므로 브루트포스 써도 가능
"""
import sys
sys.stdin = open("baek2231.txt")

def find_min_num(num):
    for i in range(1, num):
        j = i
        total = 0
        while j > 0:
            total += j % 10
            j = j // 10
        # 생성자 중 최솟값을 찾아야 하므로
        if total + i == num:
            return i
    # 생성자 없는경우 0 출력! 문제 잘 읽자
    return 0

N = int(input())
answer = find_min_num(N)
print(answer)