import sys
sys.stdin = open("baek10952.txt")


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break   
    print(A+B)