import sys
sys.stdin = open("baek10989.txt")
"""
정렬없이 정렬효과? 
이문제 잘 기억해두자! 
메모리 효율적으로 사용하려면 결국 해쉬 개념이 들어가야함!
10만 이하의 값을 준경우면 아래와같이 카운팅 개념을 활용!
해쉬 / 카운팅 이부분을 자유자재로 사용 가능해야한다.
"""



N = int(sys.stdin.readline())
NUMBERS = [0] * (10001)
for i in range(0, N):
    num = int(sys.stdin.readline())
    NUMBERS[num] += 1
for i in range(1, 10001):
    # 값이 있는애만 출력
    if NUMBERS[i] != 0:
        n = NUMBERS[i]
        for j in range(0, n):
            print(i)