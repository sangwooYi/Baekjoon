import sys
sys.stdin = open("baek11509.txt")

"""
현재 날라가는 화살의 높이 => 인덱스!!!

이런 아이디어를 혼자 생각할수 있어야 한다 ㅠㅠ

결국 key-value 해쉬 함수 개념의 알고리즘이다!!

범위가 큰 문제는
무조건 O(N)으로 풀 수 있게 알고리즘을 고민해야 한다.
즉, 매 순회마다 들어오는
입력 값에대한 판단을 O(1)로 해야한다는것! (즉 해쉬 개념이 반드시 들어가야함)
=> 이걸 dict로  하던, 인덱스를 이용해서 하던, 편한대로 하면 됨!
아래 문제는 dict로도 당연히 풀린다!
"""


def min_arrow(arr, n):

    count = 1
    # 높이는 1 ~ 1000000 까지
    arrows = [0] * 1000001
    # 초깃값
    arrows[arr[0]-1] = 1

    for i in range(1, n):
        now = arr[i]
        # 현재 높이의 화살이 존재하면 -1처리
        if arrows[now]:
            arrows[now] -= 1
            # 높이가 2 이상인 경우만
            if now > 1:
                arrows[now-1] += 1

        # 아니면 추가 화살 필요
        else:
            count += 1
            arrows[now-1] += 1 

    return count

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))

answer = min_arrow(H, N)
print(answer)