import re
import sys
sys.stdin = open("baek9342.txt")

"""
* 없거나 여러개
+ 는 한개거나 여러개
^ 는 시작 
& 는 끝
[] 안에는 묶음을 넣을 수 있으며
[^] 는 여기에 들어가는 애들은 제외하라는 의미
"""
regEx = "^[ABCDEF]*A+F+C+"

regTest = re.compile(regEx)
N = int(input())
for _ in range(0, N):
    cur_txt = input()

    res = regTest.fullmatch(cur_txt)
    
    if res:
        print("Infected!")
    else:
        print("Good")