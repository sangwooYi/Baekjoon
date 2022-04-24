import sys
sys.stdin = open("baek2812.txt")

"""
K는 지울수 있는 횟수!

일단 현재 가장 top 값보다 다음에오는숫자가 같거나 작으면 그냥 push
근데 만약에 큰수가 나오면 앞의 수를 지운다
근데 stack이 비어있지 않는 동안 최대 K번까지 지울수 있으며,
K 번 전부 소진하면 그 이후값은 그냥 전부 push.
그 뒤에 [:N-K] 번까지만 체크하면 끝!

문제를 제대로 이해하고 풀자!
"""


N, K = map(int, input().split())
num = input()

chance = K
stk = []
for i in range(0, N):
    # 이동안 계속 반복!
    while chance > 0 and stk:
        if stk[-1] < num[i]:
            stk.pop()
            chance -= 1
        else:
            break
    stk.append(num[i])
# 리스트를 str으로 조립할 때, .join을 활용하자 이게 훨씬 빠름!
# 실제 필요한 값보다 더 많은 값이 stk 에 쌓일 수 있으므로 N-K-1번 인덱스까지만!
print("".join(stk[:N-K]))