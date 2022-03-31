import sys
sys.stdin = open("baek5639.txt")
"""
한줄 씩 읽는건 input() 혹인 sys.stdin.readline()

모든 줄을 다 읽어와야하는 문제는 sys.stdin.readlines()로 받아올것!

\n 이 개행 없애주는게 .rstrip() 인것!!
sys.stdin.readline() 쓸때도 만약 \n 딸려나오는 상황이면 .rstrip() 붙옂주면 된다!
"""


t = sys.stdin.readlines()
nodes = [0] * len(t)
for i in range(0, len(t)):
    if i == len(t)-1:
        nodes[i] = int(t[i])
    else:
        nodes[i] = int(t[i].rstrip())

