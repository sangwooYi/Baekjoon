"""

1. 문자열 뒤에 A 추가
2. 뒤집은 후에 뒤에 B 추가

아이디어1.  
=> True이면 정방향, False이면 역방향
=> 뒤집을때마다 T/F 바뀌고
1. 현재 T일때 => 1번이면 그냥 A를 뒤에 추가
                 2번이먄 F로 바꾸고 앞에 B를 추가
2. 현재 F일때 => 1번이면 맨앞에 A를 추가
                 2번이면 T로 바꾸고 뒤에 B를 추가
=> ...

BFS로는 어떻게 해도 인덱스 에러 발생..

아이디어2.
목표 문자열을 역으로 초기 시작문자열로 바꾸어 보자!
1. 현재 T의 맨 뒤가 A면 pop
2. 현재 T의 맨 뒤가 B면 pop하고 뒤집기
이걸 T가 S가 될떄까지 하는것! 

때론 역발상도 필요하다!
"""





S = list(input())
T = list(input())

# S에서 T를 만드는과정을 역으로 진행하는 것!
while len(T) > len(S):
    # 현재 끝의 값이 A면 그냥 pop
    if T[-1] == "A":
        T.pop()
    # 현재 끝의 값이 B면 pop하고 뒤집는다.
    elif T[-1] == "B":
        T.pop()
        # 리스트나 문자열을 역순으로 뒤집는법 참고하자!
        # T = T[::-1]
        tmp = []
        for i in range(len(T)-1, -1, -1):
            tmp.append(T[i])
        T = tmp

if S == T:
    print(1)
else:
    print(0)