import sys
sys.stdin = open("baek9024.txt")


"""
두 용액과 거의 같은문제!

이분탐색으로도 풀수있다!
"""

T = int(sys.stdin.readline())
for tc in range(0, T):
    N, K = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    numbers.sort()
    
    left = 0
    right = N-1

    cnt = 0
    min_term = 9876543211
    while left < right:
        
        now_sum = numbers[right]+numbers[left]

        now_term = abs(K-now_sum)

        if now_term < min_term:
            min_term = now_term
            cnt = 1
        elif now_term == min_term:
            cnt += 1
        # now_sum == K  일때 left+=1 을 하던, right-=1 을 하던 둘다 맞네 ..?
        if now_sum > K:
            right -= 1
        elif now_sum <= K:
            left += 1

    print(cnt)