import sys
sys.stdin = open("baek7490.txt")

"""
파이썬
eval 함수쓰면 엄청 쉬워지는 문제 => 실제로 근데 하드코딩 할 수도 있어야함.
=> 처음 순회할때 공백의 경우는 숫자 합치기 + 그다음 순서대로 계산만해도 될듯

+ replace 문자열 메서드!
"""

T = int(input())
for tc in range(0, T):
    N = int(input())
    answer_cases = []

    oper_cases = [[" ", "+", "-"] for _ in range(0, N-1)]
    total_cases = [[]]

    for oper_case in oper_cases:
        total_cases = [x + [y] for x in total_cases for y in oper_case]
    
    for oper_case in total_cases:
        
        tmp_str = ""
        for i in range(0, len(oper_case)):
            tmp_str += (str(i+1) + oper_case[i])
        tmp_str += str(N)
        
        eval_str = tmp_str.replace(" ", "")

        if eval(eval_str) == 0:
            answer_cases.append(tmp_str)
    for i in range(0, len(answer_cases)):
        print(answer_cases[i])
    print()