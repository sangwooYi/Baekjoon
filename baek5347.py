import sys
sys.stdin = open("baek5347.txt")


def gcd(num1, num2):

    larger = max(num1, num2)
    smaller = min(num1, num2)

    while smaller > 0: 
        tmp1 = smaller
        tmp2 = larger % smaller

        larger = tmp1
        smaller = tmp2
    return larger

N = int(input())

for _ in range(0, N):
    a, b = map(int, input().split())

    cur_gcd = gcd(a, b)

    lcm = (a*b)//cur_gcd
    print(lcm)