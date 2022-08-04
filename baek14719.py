import sys
sys.stdin = open("baek14719.txt")

"""
다시 풀어보자..

그냥 쉽게 생각하자.
1 ~ W-1번 까지 전부 순회하며

해당 포인트에서
만약 해당 blocks[i] 기준
left_max / right_max 에서 min(left_max, right_max) 값보다 blocks[i]가 작아야 물이 고일 수 있다.
=> 최대 W가 500개이기 때문에 위와같은 로직이 충분히 가능!
"""



H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, W-1):
    left_max = 0
    right_max = 0
    for j in range(i-1, -1, -1):
        if left_max < blocks[j]:
            left_max = blocks[j]
    for j in range(i+1, W):
        if right_max < blocks[j]:
            right_max = blocks[j]
    height = min(left_max, right_max)
    if height > blocks[i]:
        answer += (height-blocks[i])
print(answer)