import sys
sys.stdin = open("baek1100.txt")

MAP = [0] * 8
for i in range(0, 8):
    MAP[i] = list(input())

cnt = 0
for row in range(0, 8):
    if row % 2:
        for col in range(1, 8, 2):
            if MAP[row][col] == "F":
                cnt += 1     
    else:
        for col in range(0, 8, 2):
            if MAP[row][col] == "F":
                cnt += 1 
print(cnt)