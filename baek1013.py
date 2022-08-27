import re
import sys
sys.stdin = open("baek1013.txt")

"""
정규식 익혀두자
^ $ (),  |  +   ?   .  의미
\s, \d etc 가 뭘 의미하는지
[] , [^], [-]
자유롭게 응용이 가능해야한다!
"""

N = int(input())
# 어렵게 생각말자.. 그냥 시킨대로 하면 된다.
regEx =  "(100+1+|01)+"

regTest = re.compile(regEx)
for i in range(0, N):
    case = input()
    
    # 일부만 매칭확인은 .match (정규식 만족하는 substring을 반환), 전체 확인은 .fullMatch(풀매칭아니면 None 반환)
    res = regTest.fullmatch(case)
    
    if res:
        print("YES")
    else:
        print("NO")