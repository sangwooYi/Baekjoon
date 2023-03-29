"""
항상 예외를 잘 생각하자
가장 쉬운 예외는 경계선임!
"""

def is_pelindrome(num):
    numTxt = str(num)
    flag = True
    for i in range(0, len(numTxt)//2):
        if numTxt[i] != numTxt[len(numTxt)-1-i]:
            flag = False
            break
    return flag


def find_min(num):
    prime_numbers = [2, 3]
    if num <= 2:
        return 2
    if num <= 3:
        return 3
    # N이 1000000 일 때 답이 1003001 이므로 그냥 넉넉하게 110만까지만
    for i in range(5, 1100001, 2):
        flag = True
        for j in range(0, len(prime_numbers)):
            if prime_numbers[j]**2 > i:
                break
            # 나누어 떨어지면 종료
            if i % prime_numbers[j] == 0:
                flag = False
                break
        # 소수인것
        if flag:
            prime_numbers.append(i)
            if i >= num and is_pelindrome(i):
                return i

N = int(input())

answer = find_min(N)
print(answer)