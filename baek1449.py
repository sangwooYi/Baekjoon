import sys
sys.stdin = open("baek1449.txt")


"""
오름차순 정렬 후
start 위치부터 > start+i 번쨰 위치까지 간격이 L-1 이 이하가 유지될때가지 체크
=> 이걸 넘어가는 순간 count +1 해준 후, start+i번째를 다시 start로 갱신
"""


N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

count = 1
now = 0
idx = 1
while idx < N:
    cur_len = arr[idx]-arr[now]

    if cur_len > L-1:
        count += 1
        now = idx
    idx += 1
print(count)


