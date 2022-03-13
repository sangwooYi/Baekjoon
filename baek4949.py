import sys
sys.stdin = open("baek4949.txt")

"""
소괄호, 중괄호 각각 스택을 생성


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

    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def is_empty(self):
        return self.data <= 0


def is_right_sentences(sentences):
    result = [0] * len(sentences)
    for i in range(0, len(sentences)):
        flag = True
        stk = Stack(len(sentences[i]))
        for idx in range(0, len(sentences[i])):
            if sentences[i][idx] == "(":
                stk.push(sentences[i][idx])
            elif sentences[i][idx] == "[":
                stk.push(sentences[i][idx])
            elif sentences[i][idx] == ")":
                # 스택이 비어있는데 ) 나왔으면 no
                if stk.is_empty():
                    result[i] = "no"
                    flag = False
                    break
                # 현재 pop 된게 ( 인 경우만 계속, 아니면 break
                temp = stk.pop()
                if temp == "(":
                    continue
                result[i] = "no"
                flag = False
                break
            elif sentences[i][idx] == "]":
                if stk.is_empty():
                    result[i] = "no"
                    flag = False
                    break
                temp = stk.pop()
                if temp == "[":
                    continue
                flag = False
                result[i] = "no"
                break
        # 다 통과했으면 스택 비었는지 체크,
        # 두 스택 모두 비어있는상태면 yes 아니면 no
        if flag:
            if stk.is_empty():
                result[i] = "yes"
            else:
                result[i] = "no"
    return result


MAP = []
while True:
    temp = list(input())
    if temp[0] == ".":
        break
    MAP.append(temp)
answer = is_right_sentences(MAP)
for i in range(0, len(answer)):
    print(answer[i])