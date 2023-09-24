N = int(input())

# 홀수 행이면 홀수 열만 출력 / 짝수행이면 짝수행만 출력
for i in range(0, 2*N):
    
    if i % 2:
        for j in range(0, N):
            if j % 2:
                print("*", end="")
            else:
                print(" ", end="")

    else:
        for j in range(0, N):
            if j % 2:
                print(" ", end="")
            else:
                print("*", end="")
    if i < 2*N-1:
        print()