import sys
sys.stdin = open("baek1076.txt")


regist_map = {"black": [0, 1], "brown": [1, 10], "red": [2, 100], 'orange': [3, 1000], "yellow": [4, 10000]
              ,"green": [5, 10**5], "blue": [6, 10**6], "violet": [7, 10**7], "grey": [8, 10**8], "white": [9, 10**9]}

arr = [0] * 3

for i in range(0, 3):
    arr[i] = input()

regist = 10*regist_map[arr[0]][0] + regist_map[arr[1]][0]
regist *= regist_map[arr[2]][1]
print(regist)