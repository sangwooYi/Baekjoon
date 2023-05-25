import sys
sys.stdin = open("baek13414.txt")



K, L = map(int, sys.stdin.readline().split())

"""
idea 
그냥 L짜리 값 담을 리스트 만들고
visited 배열도 L짜리 만든다. (기본값이 True)
무조건 값을 추가 + 본인의 인덱스 dict에 저장
=> 근데 만약 이미 등장했던 값이 또 나오면
=> dict에 저장된 인덱스값 false 처리, 그리고 현재 인덱스값으로 덮어쓰고 
값 리스트에 값 저장
"""
check_dict = {}
answer_list = [0] * L
visited = [True] * L
for idx in range(0, L):
    # 문자열로 간주하자
    cur = sys.stdin.readline().rstrip()

    answer_list[idx] = cur
    if cur in check_dict.keys():
        prev_idx = check_dict[cur]
        visited[prev_idx] = False
    check_dict[cur] = idx
    answer_list[idx] = cur

cnt = 0
for i in range(0, L):
    if visited[i]:
        print(answer_list[i])
        cnt += 1
    if cnt == K:
        break

