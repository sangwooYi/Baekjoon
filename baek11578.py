import sys
sys.stdin = open("baek11578.txt")



def comb(in_arr, visited, start, n, r, m):
    global is_clear
    global answer

    all_clear_score = 2**N-1

    if r == 0:
        
        tmp = [0] * m
        idx = 0
        for i in range(0, n):
            if visited[i]:
                tmp[idx] = in_arr[i]
                idx += 1
        check_score = 0
        for i in range(0, len(tmp)):
            check_score |= tmp[i]
        if check_score == all_clear_score:
            is_clear = True
            answer = min(answer, m)
        return
    
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(in_arr, visited, i+1, n, r-1, m)
        visited[i] = False

# N 문제수 , M 학생수
N, M = map(int, input().split())
students_score = [0] * M
for i in range(0, M):
    tmp_arr = list(map(int, input().split()))
    can_solve = tmp_arr[1:]

    binary_sum = 0
    for j in range(0, len(can_solve)):
        binary_sum += 2**(can_solve[j]-1)
    students_score[i] = binary_sum

is_clear = False
answer = M
for i in range(1, M+1):
    visited = [False] * M
    comb(students_score, visited, 0, M, i, i)
if not is_clear:
    answer = -1
print(answer)