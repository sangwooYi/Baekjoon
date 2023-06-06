import sys
sys.stdin = open("baek7785.txt")

N = int(sys.stdin.readline().rstrip())

check_dict = {}
for i in range(0, N):
    name, oper = sys.stdin.readline().split()
    
    check_dict[name] = oper
    
answer = []
for name in check_dict:
    if check_dict[name] == "enter":
        answer.append(name)

answer.sort(reverse=True)
for i in range(0, len(answer)):
    print(answer[i])