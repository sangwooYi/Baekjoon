import sys
sys.stdin = open("baek11723.txt")

"""
만약 메모리가 충분하면 사실 리스트 풀이가 더 좋으나
메모리가 적게 주어졌으므로
진짜 집합을 사용할것!


집합도 사용할 줄 알아야 한다!
remove() => 지우려는 값이 없으면 keyError를 발생
discard() => 지우려는 값이 없으면 그냥 무시 (정상 진행)
"""




M = int(sys.stdin.readline())
S = set()
for i in range(0, M):
    arr = sys.stdin.readline().split()
    if arr[0] == "all":
        S = set([i for i in range(1, 21)])
    elif arr[0] == "empty":
        S = set()
    else:
        x = int(arr[1])
        if arr[0] == "add":
            S.add(x)
        elif arr[0] == "remove":
            S.discard(x)
        elif arr[0] == "check":
            # 집합도 a in 집합 T/F 판별이 가능하다!
            if x in S:
                print(1)
            else:
                print(0)
        elif arr[0] == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)