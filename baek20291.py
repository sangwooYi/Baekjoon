import sys
sys.stdin = open("baek20291.txt")


N = int(input())

file_map = {}

for i in range(0, N):
    cur = input()

    fileName, extension = cur.split(".")
    
    if extension in file_map.keys():
        file_map[extension] += 1
    else:
        file_map[extension] = 1

key_arrs = list(file_map.keys())
key_arrs.sort()

for key in key_arrs:
    print(f"{key} {file_map[key]}")