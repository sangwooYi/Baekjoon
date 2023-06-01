import sys
sys.stdin = open("baek22233.txt")


N, M = map(int, sys.stdin.readline().split())

res_cnt = N
keywords = {}
for i in range(0, N):
    word = sys.stdin.readline().rstrip()
    keywords[word] = 1

for i in range(0, M):
    cur_words = list(sys.stdin.readline().rstrip().split(","))    
    for cur_word in cur_words:
        if cur_word in keywords.keys():
            if keywords[cur_word]:
                keywords[cur_word] = 0
                res_cnt -= 1

    print(res_cnt)