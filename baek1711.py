import sys
sys.stdin = open("baek1711.txt")

"""
피타고라스
C**2 = a**2 + b**2
"""
def distance_square(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def is_right_angle(p1, p2, p3):
    a_square =  distance_square(p1, p2)
    b_square = distance_square(p2, p3)
    c_square = distance_square(p1, p3)

    total = a_square + b_square + c_square
    hypo = max(a_square, b_square, c_square)

    if hypo == total-hypo:
        return True
    else:
        return False



N = int(input())
coords = [0] * N
for i in range(0, N):
    coords[i] = list(map(int, input().split()))

answer = 0
for i in range(0, len(coords)-2):
    for j in range(i+1, len(coords)-1):
        for k in range(j+1, len(coords)):
            if is_right_angle(coords[i], coords[j], coords[k]):
                answer += 1
print(answer)