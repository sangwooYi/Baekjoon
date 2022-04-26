import sys
sys.stdin = open("baek1991.txt")
"""
전위, 중위, 후위 순회의 기본중의 기본임!
여기서 응용까지 가능해야한다.
"""



def pre_order(node):
    global pre_ord
    if node:
        idx = alph_dict[node]
        pre_ord += node
        pre_order(left[idx])
        pre_order(right[idx])

def in_order(node):
    global in_ord
    if node:
        idx = alph_dict[node]
        in_order(left[idx])
        in_ord += node
        in_order(right[idx])


def post_order(node):
    global post_ord
    if node:
        idx = alph_dict[node]
        post_order(left[idx])
        post_order(right[idx])
        post_ord += node

N = int(input())
left = [0] * (N+1)
right = [0] * (N+1)
alph_dict = {}
for i in range(0, N):
    node, l, r = input().split()
    alph_dict[node] = i+1
    if l != ".":
        left[i+1] = l
    if r != ".":
        right[i+1] = r

pre_ord = ""
in_ord = ""
post_ord = ""
pre_order("A")
in_order("A")
post_order("A")
print(pre_ord)
print(in_ord)
print(post_ord)
