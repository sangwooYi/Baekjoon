import re

"""
정규식 익혀두자!
"""

case = input()
regEx = "(100+1+|01)+"

regTest = re.compile(regEx)
res = regTest.fullmatch(case)
if res:
    print("SUBMARINE")
else:
    print("NOISE")