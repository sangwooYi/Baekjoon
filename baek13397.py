import sys
sys.stdin = open("baek13397.txt")


"""
전략

이분탐색 진행

이분 탐색에서 핵심은
1. left / right를 어떻게 잡을 것인가
2. mid 값의 정의는 무엇인가 (또 어떤 방식으로 탐색 기준을 정하는가)
3. 탐색후 mid 값을 어떤기준으로 줄이거나 or 늘릴것인가.
=> 이걸 통해 단순 binary search 인지 lower bound 인지 upper bound 인지를 가를 수 있다.
시작값은
left 는 그냥 0 <= 구간 요소가 1개만있을때 최대-최소 차가 0이므로! (이부분이 내가 틀렸던 이유)
right는 그냥 10000 (이 문제에서의 최대치 or 그냥 전체 요소의 최댓값)

그다음 mid 는 각 구간 최대-최소 차중 최댓값
따라서 현재 포인트 기준 다음 포인트에서 최대-최소 차가 mid를 넘어가면 구간을 쪼갬
근데 M개 이하로 그룹을 쪼개야한다 따라서
=> 현재 기준으로 쪼갤때 M 개 그룹이하로 나오면 (조건 만족) 
근데 더 작은 값으로 안되는지 mid 값줄인다. 
=> M개 그룹 초과로나오면 (너무 작은값을 기준으로 쪼갠 것) 다음 탐색구간 늘린다.

따라서 lower bound
"""

def binary_search_left():
    
    left = 0
    right = max(numbers)

    while left < right:
        mid = (left+right)//2

        group_cnt = 1
        now_min = numbers[0]
        now_max = numbers[0]

        for i in range(1, N):
            now_min = min(numbers[i], now_min)
            now_max = max(numbers[i], now_max)

            # 다음 탐색 요소를 진행할때 최대-최소 차가 mid보다 커지면 그룹을 쪼개야 함
            if now_max-now_min > mid:
                group_cnt += 1
                # 최대/최소 값도 갱신해 주어야 함
                now_min = numbers[i]
                now_max = numbers[i]

        # 다음 탐색값을 더 키운다
        if group_cnt > M:
            left = mid+1
        else:
            right = mid
    return left



N, M = map(int, input().split())
numbers = list(map(int, input().split()))

answer = binary_search_left()
print(answer)