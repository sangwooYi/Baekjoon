import sys
sys.stdin = open("baek9017.txt")


T = int(input())

for tc in range(0, T):
    N = int(input())

    arr = list(map(int, input().split()))
    
    cnt_map = {}
    point_map = {}

    for num in arr:
        if num in cnt_map.keys():
            cnt_map[num] += 1
        else:
            cnt_map[num] = 1
    # 6명 이상 출전해야만 가능
    for key in cnt_map:
        if cnt_map[key] >= 6:
            # 유효한 팀만 point map에 추가
            # 카운팅, 상위 4명의 총점, 5번째 점수를 저장
            point_map[key] = [0, 0, 0]
    point = 1
    for num in arr:
        if num in point_map.keys():
            cur_cnt = point_map[num][0]

            if cur_cnt == 4:
                # 5번째 선수
                point_map[num][2] = point
            elif cur_cnt < 4:
                point_map[num][1] += point
            point += 1
            point_map[num][0] += 1
    result = [0] * len(point_map)
    idx = 0
    for key in point_map:
        cnt, total_top4, fifth_point = point_map[key]
        result[idx] = [total_top4, fifth_point, key]
        idx += 1
    result.sort(key=lambda x : (x[0], x[1]))
    print(result[0][2])
    