def GCD(a, b):
    
    larger = max(a, b)
    smaller = min(a, b)

    while smaller > 0:
        next_l = smaller
        next_s = larger % smaller
        larger = next_l
        smaller = next_s
    return larger


T = int(input())
for i in range(0, T):
    A, B = map(int, input().split())

    gcd = GCD(A, B)
    lcm = (A*B)//gcd
    print(lcm)