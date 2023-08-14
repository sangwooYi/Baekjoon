"""
최대 연산수 약 65000회
따라서 그냥 브루트포스로 가능
"""

N = int(input())

num = 1

flag = False
while True:
    cur =  (num*(num+1))//2 
 
    if cur > N:
        break
    if cur == N:
        flag = True
        break
    num += 1


if flag:
    print(num)
else:
    print(num-1)