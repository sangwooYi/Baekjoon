import sys
sys.stdin = open("baek1654.txt")
"""
우선 최대 공약수로 가정
=> 최대 공약수일때 나오는 조각수 확인 
>= N이면 그냥 Okay
만약 < N 이면 계속 줄여야 함
유클리드 호제법 기억하자 아래가 유클리드 호제법 코드
=> 이 문제는 최대공약수 문제는 아님
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_gcd_in_arr(arr):
    gcd_arr = arr[0]
    for i in range(0, len(arr)):
        # 현재 gcd 값과 다음 arr 요소를 꼐산하여 gcd를 계속 계산
        gcd_arr = gcd(gcd_arr, arr[i])
    return gcd_arr

sys.stdin.readline() 입력방법도 알아두자(입력받는 양 자체가 많을때 겁나 유용)


이분탐색! 
logN 시간복잡도기때문에 2^31 같이 괴랄한 수의 범위라도 금방 찾을 수 있다.
이렇게 괴랄한 숫자 범위를 줄때는
이분 탐색을 한번쯤 떠올릴 수 있어야 함

요거는 무조건 다시 한번 풀어 보자,.
"""

def find_max_parts(arr, num, largest):
    min = 0
    # 반드시 최댓값보다 1 큰수여야 한다.
    # 주어진 길이가 1, 1 인경우도 있을 수 있으므로 살짝의 트릭을 준 것! 
    max = largest + 1
  
    while min < max:
        print(min ,max)
    
        #  // 2   java 정수 / 2  무조건 소숫점을 버림
        mid = (min + max) // 2
        count = 0
        for i in range(0, len(arr)):
            count += arr[i] // mid
        # 현재 count가 필요갯수보다 적으면 더 작게 잘라야함!
        # 이부분이 이분 탐색 지점
        if count < num:
            max = mid
        # 문제 조건 자체이서는 count >= num 이거기만 만족하거든 조건을 그 중에서 가장 길이가 큰놈
        #  
        else:
            # mid + 1을 해줌으로써 min과 max가 같아지는 순간이 온다. 그떄가 upper bound
            min = mid + 1
    #
    # 그렇게 계산하다가 min 값이 max값 이상이 되는 첫 경우를 답으로 반환 
    # min = mid+1을 통해 upperbound를 계산하므로 결과값은 1을 오히려 뺴주어야 한다.
    return min - 1

K, N = map(int, input().split())
strs = []
max_len = 0
for i in range(0, K):
    now = int(input())
    if max_len <= now:
        max_len = now
    strs.append(now)
answer = find_max_parts(strs, N, max_len)
print(answer)