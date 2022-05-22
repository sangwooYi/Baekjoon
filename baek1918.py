import sys
sys.stdin = open("baek1918.txt")

"""
알아두면 좋은 알고리즘!
스택 + 우선순위를 이용한다.

icp (in-coming priority) = 진입 우선순위
isp (in-stack priority)  = 내부 스택 우선순위
     (  )   +  -   * /
icp  3  -   1       2
isp  0  -   1       2
기본적인 로직
토큰이 연산자인 경우 스택의 top과 비교
해당 연산자의 진입 우선순위가 높으면 스택에 push
아니면 pop()
현재 연산자 토큰과 (icp), 스택 내부 top (isp)의 토큰끼리의 우선순위를 비교
if (icp > isp) {
    # 진입우선순위가 높은 경우만 push
    push()
} else{
    # icp > isp 를 만날때까지 pop
    while icp <= isp {
        pop()
    }
    push()
}
여기서 ( 는 무조건 push
)는 ( 나올때까지 pop
"""

class Stack:

    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.data = 0
        self.ptr = 0

    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.data += 1
        self.ptr += 1
        return x
    
    # top에있는 값을 아예 뺀다음 반환 (이게 pop)
    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        self.data -= 1
        now = self.stk[self.ptr]
        return now

    # top에 있는 값을 보여줌
    def peek(self):
        return self.stk[self.ptr-1]

    
    def is_empty(self):
        return self.data <= 0




in_notice = list(input())
answer = ""

# 진입 우선 순위
icp = {"(": 3, "+": 1, "-": 1, "*": 2, "/": 2}
# 내부 스택 우선순위
isp = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
check_list = ["+", "-", "/", "*"]

stk = Stack(len(in_notice)*2)


# 중위표기식 -> 후위표기식 만드는 방법 공식이니까 그냥 외워버리자! 로직은 간단함!
# 현재 토큰이 피연산자 => 그냥 답안에 추가
# ( => 무조건 push  )  => ( 나올때까지 pop
# 연산자인 경우 => icp > isp 인경우 push
# 아니면 현재 진입 토큰의 icp 보다 isp가 낮은 경우 나올떄까지 pop 
for i in range(0, len(in_notice)):
    now = in_notice[i]
    # ( 는 무조건 push
    if now == "(":
        stk.push(now)
    # ) 는 ( 나올떄까지 pop 그 과정에 나오는 연산자들은 answer에 추가
    # 문제에서 괄호가 잘못된 경우는 없다!
    elif now == ")":
        while stk.peek() != "(":
            tmp = stk.pop()
            answer += tmp
        # 현재 peek가 가르키는 값은 ( 얘는 그냥 버린다.
        stk.pop()
    # 토큰이 연산자인 경우
    elif now in check_list:
        # 스택이 비어있으면 그냥 push만
        if stk.is_empty():
            stk.push(now)
        # 스택에 값이 있는 경우
        else:
            # icp > isp  인 경우
            if icp[now] > isp[stk.peek()]:
                stk.push(now)
            # 스택 top의 isp 값이 우선순위가 낮지 않은 경우
            else:
                # 스택 top의 isp값이 낮은애가 나올떄까지 pop // stk이 비어있으면 바로 push
                while not stk.is_empty() and icp[now] <= isp[stk.peek()]:
                    tmp = stk.pop()
                    answer += tmp
                # 그러고는 push
                stk.push(now)
    # 피연산자
    else:
        answer += now
# 혹시 스택에 남은 연산자들 있으면 전부 배출
while not stk.is_empty():
    answer += stk.pop()
print(answer)

                
