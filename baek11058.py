import sys
sys.stdin = open("baek11058.txt")

"""
복사붙여넣기를 할때 최소 3개 버튼이 필요하다
=> 이건 복사 후에 , 붙여넣기 4개 이상부터는, 
다시 복사해서 붙여넣는게 더 효율적인것!

따라서 최댓값을 위한 연속 붙여넣기 횟수는 3회가 최대!
=> 이걸 생각해내는게 포인트였음.. 어렵다 ...

꼭 다시 풀어 보자 !
"""

N = int(input())
# 초깃값 그냥 A만 출력하 경우
DP = [i for i in range(0, N+1)]

for i in range(7, N+1):
    DP[i] = max(DP[i-3]*2, DP[i-4]*3, DP[i-5]*4)
print(DP[N])