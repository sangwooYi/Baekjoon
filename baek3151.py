import sys
sys.stdin = open("baek3151.txt")


N = int(input())
groups = list(map(int, input().split()))
groups.sort()



cnt = 0
# 1번인덱스 ~ N-2번인덱스까지가 i
for i in range(0, N-2):
    # 기준을 0 ~ N-2번까지 잡고 그 우측에 있는 나머지 원소중 2개를 뽑는 형태로 진행!
    start = i+1
    end = N-1
    max_idx = N
    while start < end:

        # 중복 방지
        now_sum = groups[start] + groups[i] + groups[end]

        # 여기가 핵심
        if now_sum == 0:
            # 정렬한 값이므로 start ~ end까지는 모두 같은 원소인것! 따라서 end-start 만큼 경우가 존재 
            # 어차피 now_sum 이 0인경우 start를 1 늘려주므로 이렇게 해도 되는 것!
            # ex) [-1, 5, 5, 5]  start가 1일때는 1, 3 // 1, 2 그다음 start가 2일때 2, 3
            # 결국 이런식으로 다 탐색할 수 있게 됨
            if groups[start] == groups[end]:
                cnt += (end-start)
            else:
                if max_idx > end:
                    max_idx = end
                    # 위와 같은 원리로 start는 어차피 다음 탐색에서 늘려주므로, 현재 end 원소와 같은 원소가 몇개 존재하는지만 체크하면 충분!
                    while max_idx >= 0 and groups[max_idx-1] == groups[end]:
                        max_idx -= 1
                cnt += (end-max_idx+1)
            start += 1
        elif now_sum > 0:
            end -= 1
        else:
            start += 1

print(cnt)