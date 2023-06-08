"""
열은 2N-1열로 이루어지며
가장 처음/ 가장 마지막 열은 
N번 * 출력, 2N-3 공백, N번 * 출력

"""

# N = int(input())
N = 5

center_idx = (2*N-1)//2
for i in range(0, 2*N-1):
    # 첫열, 마지막열
    if i == 0 or i == 2*N-2:
        for j in range(0, N):
            print("*", end="")
        for j in range(0, 2*N-3):
            print("", end=" ")
        for j in range(0, N):
            print("*", end="")
    # 중간
    if i == center_idx:
        for j in range(0, N-1):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")
        print("*", end="")           
    if i > 0 and i < center_idx:
        for j in range(0, i):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")
        print("*", end="")
        for j in range(0, 2*N-3-2*i):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")
        print("*", end="") 
    if i > center_idx and i < 2*N-2:
        for j in range(0, 2*N-2-i):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")
        print("*", end="")
        for j in range(0, 2*i-(2*N-1)):
            print("", end=" ")
        print("*", end="")
        for j in range(0, N-2):
            print("", end=" ")                    
        print("*", end="")
    print(" ")