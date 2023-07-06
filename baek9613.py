import sys
sys.stdin = open("baek9613.txt")

"""
gcd 구하는 방법 기억하자

a > b 일때

while b > 0:
    a, b = b, a%b
return a

"""

def calc_gcd(a, b):

    small_num = min(a, b)
    large_num = max(a, b)

    while small_num > 0:
        tmp = small_num
        small_num = large_num%small_num
        large_num = tmp
    return large_num



T = int(input())
for _ in range(0, T):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    nums = tmp[1:]
    
    ans = 0
    for i in range(1, N):
        for j in range(0, i):
            num1 = nums[i]
            num2 = nums[j]
            cur_gcd = calc_gcd(num1, num2)
            ans += cur_gcd
    print(ans)