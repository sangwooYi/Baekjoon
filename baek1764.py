import sys
sys.stdin = open("baek1764.txt")

"""
배열이나 리스트 탐색같은경우는 자료의 크기에따라 O(N)에 시간복잡도를 가지나
해쉬에 경우 .keys() 는 해쉬값에 매칭되어 저장되므로,
아무리 딕셔너리가 커져도 O(1) 이다!! 해당 해쉬값이 있냐 없냐만 판단해주는것!
따라서 압도적인 시간차이가 난다.!
"""


N, M = map(int, input().split())
NO_LISTEN = [0] * N
temp_dict = {}
# NO_SEE = [0] * M
for i in range(0, N):
    NO_LISTEN[i] = input()
    temp_dict[NO_LISTEN[i]] = i

temp = [0] * 500000
count = 0
for i in range(0, M):
    now = input()
    if now in temp_dict.keys():
        temp[count] = now
        count += 1
print(count)
if count > 0:
    ans = temp[:count]
    ans.sort()
    for i in range(0, count):
        print(ans[i])
