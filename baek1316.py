import sys
sys.stdin = open("baek1316.txt")

def is_group_string(string):

    check_dict = {}
    
    tmp = string[0]
    check_dict[string[0]] = 1
    for i in range(1, len(string)):
        if tmp != string[i]:
            if string[i] in check_dict.keys():
                return False
            check_dict[tmp] = 1
        tmp = string[i]
    return True
            

N = int(input())
answer = 0
for i in range(0, N):
    now = list(input())
    if is_group_string(now):
        answer += 1
print(answer)