import sys
sys.stdin = open("baek5525.txt")

"""
이런 문제도 혼자서 풀 수 있어야 한다!

"""


N = int(input())
M = int(input())
P = input()
# 문자열로 패턴 만들고 일일이 비교 (100만개니까 충분히 가능)
# 패턴의 길이는 2N + 1길이만큼이다!
pattern = "I" + ("OI") * N
    
answer = 0
idx = 0
count = 0
while idx < (M-1):
    if P[idx:idx+3] == "IOI":
        idx += 2
        count += 1
        # 패턴은 계속 OIOI가 반복되므로 아래처럼 진행하는게 핵심아이디어!
        if count == N:
            answer += 1
            # 이부분이 핵심 아이디어다!
            count -=1
    # 패턴이 꺠지면 count 초기화 한후, 인덱스 하나만 이동
    else:
        idx += 1
        count = 0

print(answer)