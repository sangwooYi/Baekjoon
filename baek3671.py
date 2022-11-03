import sys
sys.stdin = open("baek3671.txt")


def is_prime(num):
    
    flag = True
    for prime in primes:
        if prime**2 > num:
            break
        if num % prime == 0:
            flag = False
            break
    return flag

def perm(arr, out, visited, n, r, depth):
    global cnt 

    if depth == r:
        tmp_str = "".join(out)
        tmp_num = int(tmp_str)
        if tmp_num < 2:
            return
        if tmp_num not in check_dict.keys():
            if is_prime(tmp_num):
                check_dict[tmp_num] = 1
                cnt += 1
        return
        
    for i in range(0, n):
        if visited[i]:
            continue
        visited[i] = True
        out[depth] = arr[i]
        perm(arr, out, visited, n, r, depth+1)
        visited[i] = False

N = int(input())
test_cases = [0] * N
for i in range(0, N):
    test_cases[i] = list(input())


primes = [2, 3]
# 소수 판별, 2를 제외하고는 짝수는 어차피 소수가 아님
# 즉 5이후부터 홀수만 따지면 되며, 해당 숫자의 제곱근까지만 체크하면 됨! (대칭구조!)
# 이를통해 10**6 이라도 10**3 까지만 체크하면 되는것
upper = int(10000000**(1/2))
for i in range(5, upper+1, 2):
    flag = False
    for j in range(0, len(primes)):
        if primes[j]**2 > i:
            break
        if i % primes[j] == 0:
            flag = True
            break
    if not flag:
        primes.append(i)

for test_case in test_cases:
    cnt = 0
    # 중복 제거용
    check_dict = {}
    arr_len = len(test_case)

    for i in range(1, arr_len+1):
        visited = [False] * arr_len
        out = [0] * i
        perm(test_case, out, visited, arr_len, i, 0)
    print(cnt)