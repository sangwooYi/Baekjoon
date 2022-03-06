import sys
sys.stdin = open("sort_char.txt")

"""
key lambda 연습문제!!

정렬을 두번 이상해야하는 경우는 그냥 key lambda 사용하자!

사용법
배열.sort(key = lambda x : (첫번째 정렬기준, 그다음 정렬기준 ... ))
"""

# int(input())   == nextInt()
N = int(input())
words_with_length = []
for i in range(0, N):
    # word = 해당 줄에 string
    word = input()
    words_with_length.append([word, len(word)])

print(words_with_length)


words_with_length.sort(key=lambda x : (x[1], x[0]))

temp = []
for i in range(0, len(words_with_length)):
    now = words_with_length[i][0]
    if i == 0:
        print(now)
        temp.append(now)
    else:
        if now in temp:
            continue
        print(now)
        temp.append(now)
