import sys
sys.stdin = open("baek1759.txt")

"""
중요한게
최소 
한개의 모음,
두개의 자음을 갖고 있어야 한다.
즉 이걸 체크해야함!
"""
def is_crypto(arr):
    vowel_cnt = 0
    consonant_cnt = 0

    for i in range(0, len(arr)):
        if arr[i] in vowels.keys():
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        return True
    return False

def comb(arr, visited, start, n, r, k):
    if r == 0:
        tmp = [0] * k
        idx = 0
        for i in range(0, n):
            if visited[i]:
                tmp[idx] = arr[i]
                idx += 1
        # 암호 조건 맞을때만 
        if is_crypto(tmp):
            tmp.sort()
            tmp_str = "".join(tmp)
            result.append(tmp_str)
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, visited, i+1, n, r-1, k)
        visited[i] = False


L, C = map(int, input().split())
letters = list(input().split())
visited = [0] * C
vowels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
result = []
comb(letters, visited, 0, C, L, L)
result.sort()
for i in range(0, len(result)):
    print(result[i])