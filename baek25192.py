import sys
sys.stdin = open("baek25192.txt")


N = int(sys.stdin.readline().rstrip())

cnt_map = {}

answer = 0
for i in range(0, N):
    cur = sys.stdin.readline().rstrip()
    
    if cur == "ENTER":
        cnt_map = {}
    else:
        if cur not in cnt_map.keys():
            cnt_map[cur] = 1
            answer += 1
print(answer)