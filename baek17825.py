import sys
sys.stdin = open("baek17825.txt")
"""
인덱스기준 
인덱스 4에 도착 => 다음부턴 part2로 진행
인덱스 9에 도착 => 다음부턴 part3로 진행
인덱스 14에 도착 => 다음부터는 part4로 진행

이건 풀고나서도 다른분들 풀이한번 보자..
"""

nums = list(map(int, input().split()))
part1 = [2*i for i in range(1, 21)]
part2 = [13, 16, 19, 25, 30, 35, 40]
part3 = [20, 24, 25, 30, 35, 40]
part4 = [28, 27, 26, 25, 30, 35, 40]


print(part1)