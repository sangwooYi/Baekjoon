A, P = map(int, input().split())

save_map = {A: 1}

cnt = 1
now = A
while True:
    
    now_str = str(now)
    tmp = 0
    
    for i in range(0, len(now_str)):
        tmp += (int(now_str[i])**P)
    if tmp not in save_map.keys():
        cnt += 1
        save_map[tmp] = cnt
        now = tmp
    else:
        pos = save_map[tmp]
        
        print(pos-1)
        break
        