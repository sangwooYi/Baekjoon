"""
소수 구하는 방법 까먹지 말자!
포인트는, 
1. 홀수만 체크 하면 된다.

2. 매 체크마다 현재까지 누적된 소수들 중에서, 나누어 떨어지는 애가 없는지 체크
=> 근데 이 범위는 (현재 값) > (이전 소수)**2 범위까지만! 
(10 * 10) 을 예로 들면
1 * 100
2 * 50
4 * 25
5 * 20
10 * 10  ======= 이렇게 제곱근 기준으로 좌우 대칭을 이루므로 제곱근까지만 체크하면 되는것!
20 * 5
25 * 4
50 * 2
100 * 1


투포인터 알고리즘 === 슬라이딩 윈도우

단순히 크기가 정해진 문제가 일반적이나,
이 문제처럼 조건에 따라 start, end 포인트를 움직이는 문제도 존재한다!

소수 배열은 오름차순 정렬이 되어있으므로
start, end 우선 0으로 시작
1. 현재 구간까지 합 < N 이면 end 포인트를 1증가
2. 현재 구간까지 합 > N 이면 start포인트를 1증가
3. 현재 구간까지 합이 == N 이면 카운트하고 start 포인트를 1증가
"""
N = int(input())

def find_prime(n):
    primes = [2, 3]
    for i in range(5, n+1, 2):
        flag = False
        for j in range(0, len(primes)):
            # 현재 소수가, 지금 값의 제곱보다 커지면 더 이상 볼 필요가 없다
            if primes[j]**2 > i:
                break
            if i % primes[j] == 0:
                flag = True
                break
        if not flag:
            primes.append(i)
    return primes


# 우선 N 이하의 수에서의 모든 소수를 체크
prime = find_prime(N)

answer = 0

start = 0
end = 0
    
# 요것도 슬라이딩 윈도우(투포인터 알고리즘) 이라고 한다!
while start < len(prime) and end < len(prime):
    tmp_sum = 0
    for i in range(start, end+1):
        tmp_sum += prime[i]
    
    # N 보다 구간합이 작으면 end를 1 증가
    if tmp_sum < N:
        end += 1

    # N보다 구간합이 이상이면 start를 1 증가
    else:
        # 같을때는 카운트   
        if tmp_sum == N:
            answer += 1
        start += 1
print(answer)