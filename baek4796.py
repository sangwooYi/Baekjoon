import sys
sys.stdin = open("baek4796.txt")

tc = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    mok = V//P
    mod = V%P

    add_val = mod
    if mod > L:
        add_val = L

    answer = mok*L + add_val
    print(f"Case {tc}: {answer}")

    tc += 1

