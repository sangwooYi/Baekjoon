import sys

sys.stdin = open("baek9576.txt")

"""
전략1.
1000 * 1000 = 100만이니까 가능한 전략

책 권수에 맞게 배열을 선언하고,
신청자가 원하는 구간을 체크해서 학생별로 1씩 증가
+ hepq 에 학생 신청 범위를 기준으로 hepaq에 저장
즉 신청 범위가 작은 학생 순으로 순회하며
그 학생이 신청한 책 범위중 가장 적은 신청 범위의 책을 지급
=> 얘는 결국 안되었다.. 이유를 잘 모르겠음


전략 2.
a - b범위의 책을 신청할 때
b를 기준으로 오름차순 정렬
범위중 가장 번호가 낮은 책부터 지급
=> 회의실 배정과 유사한 문제임!
그리디는 전략 2처럼 보다 명쾌한 방법이어야 한다!

"""

# 전략1 내 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     hq = []
#     hope_count = [0] * (N+1)
#     visited = [False] * (N+1)
#     answer = 0
#     for i in range(0, M):
#         a, b = map(int, input().split())
#         for j in range(a, b+1):
#             hope_count[j] += 1
#         # 신청 부수
#         count = b-a+1
#         # 신청부수를 기준으로 신청 범위와 함께 저장
#         heapq.heappush(hq, (count, a, b))
#     while hq:
#         # 신청부수가 적은 사람순으로
#         now = heapq.heappop(hq)
#         start = now[1]
#         end = now[2]
        
#         # 책 지급도 역시 신청자가 적은 순으로
#         tmp_hq = []
#         for i in range(start, end+1):
#             heapq.heappush(tmp_hq, (hope_count[i], i))

#         while tmp_hq:
#             tmp = heapq.heappop(tmp_hq)
#             num = tmp[1]
#             # 이미 지급된 책이면 pass
#             if visited[num]:
#                 continue
#             # 지급 가능하면 지급처리하고 break 다음사람 봐야 함

#             visited[num] = True
#             answer += 1
#             break
#     print(answer)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # 책 신청 사람수 체크
    hope_num = [0] * (N+1)
    # 신청자에 대한 배열
    requests = [0] * M
    # 책 지급여부 체크
    visited = [False] * (N+1)

    answer = 0
    for i in range(0, M):
        a, b = map(int, input().split())
        requests[i] = [a, b]
        for j in range(a, b+1):
            hope_num[j] += 1
    requests.sort(key=lambda x : x[1])
    
    for i in range(0, M):
        start, end = requests[i]
        for j in range(start, end+1):
            if visited[j]:
                continue
            visited[j] = True
            answer += 1
            break

    print(answer)