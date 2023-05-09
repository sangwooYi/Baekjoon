"""
기본적으로 H, C, O, ) 는 그다음 인덱스에 숫자가 오는지 체크해야 함
stack 에 저장 있는 ( 갯수를 체크
( 가 없는 상태에서 H, C, O는 즉각즉각 체크
( 가 나오면 )가 나오기 전까지 계속 stack에 push
    => )가 나오면 (가 나올때까지 계속 pop
    => ) 다음이 숫자가 나오는지 체크 있으면 () 안에 질량 * 숫자 
    아니면 그냥 다음 순회 진행

만들지 못하는 경우는 없음
"""

class Stack:

    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.ptr = 0
        self.data = 0
    
    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.ptr += 1
        self.data += 1
        return x

    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        self.data -= 1
        now = self.stk[self.ptr]
        return now

    def mod_peek(self, num):
        if self.data <= 0:
            raise IndexError
        self.stk[self.ptr-1] *= num

    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.stk[self.ptr-1]

    def is_empty(self):
        return self.data <= 0

CHEM_FORMULA = list(input())

weight_depth = [0] * len(CHEM_FORMULA)

conv_dict = { "H": 1, "C": 12, "O": 16 }
digit_check = []
for i in range(2, 10):
    digit_check.append(str(i))

stk = Stack(len(CHEM_FORMULA)*2)
idx = 0

# 스택의 ( 갯수마다 + 1씩
depth_cnt = 0
while idx < len(CHEM_FORMULA):
    # 스택 비어있을 때
    if stk.is_empty():
        if CHEM_FORMULA[idx] == "(":
            depth_cnt += 1
            stk.push(CHEM_FORMULA[idx])
            idx += 1
        # 스택에 넣을 필요 X
        elif CHEM_FORMULA[idx] in conv_dict.keys():
            cur_chem = CHEM_FORMULA[idx]
            if idx < len(CHEM_FORMULA)-1 and CHEM_FORMULA[idx+1] in digit_check:
                weight_depth[0] += (conv_dict[cur_chem]*int(CHEM_FORMULA[idx+1]))
                idx += 2
            else:
                weight_depth[0] += conv_dict[cur_chem]
                idx += 1

    # 스택에 값이 있을 때 (즉 depth_cnt >= 1)
    else:
        if CHEM_FORMULA[idx] == "(":
            depth_cnt += 1
            stk.push(CHEM_FORMULA[idx])
            idx += 1
        elif CHEM_FORMULA[idx] in conv_dict.keys():
            cur_chem = CHEM_FORMULA[idx]
            if idx < len(CHEM_FORMULA)-1 and CHEM_FORMULA[idx+1] in digit_check:
                weight_depth[depth_cnt] += (conv_dict[cur_chem]*int(CHEM_FORMULA[idx+1]))
                idx += 2
            else:
                weight_depth[depth_cnt] += conv_dict[cur_chem]
                idx += 1
        elif CHEM_FORMULA[idx] == ")":

            tmp_wieght = weight_depth[depth_cnt]
            weight_depth[depth_cnt] = 0

            depth_cnt -= 1

            if idx < len(CHEM_FORMULA)-1 and CHEM_FORMULA[idx+1] in digit_check:
                weight_depth[depth_cnt] += tmp_wieght*(int(CHEM_FORMULA[idx+1]))
                idx += 2
            else:
                weight_depth[depth_cnt] += tmp_wieght
                idx += 1
            stk.pop()
#print(weight_depth[0])


# 진짜 스택을 활용한 풀이
stk2 = Stack(len(CHEM_FORMULA)*2)
check_dict = { "H": 1, "C": 12, "O": 16, "(": 0, ")": 0 }

for chr in CHEM_FORMULA:
    if chr not in check_dict:
        num = int(chr)
        stk2.mod_peek(num)
    
    elif chr == ")":
        tmp_weight = 0
        while stk2.peek() != "(":
            cur = stk2.pop()
            tmp_weight += cur
        stk2.pop()
        stk2.push(tmp_weight)
    elif chr == "(":
        stk2.push(chr)
    else:
        stk2.push(check_dict[chr])

ans = 0
while not stk2.is_empty():
    ans += stk2.pop()
print(ans)