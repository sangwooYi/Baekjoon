"""
완전 이진트리일때 구성 방법
"""
import sys


def make_bin_tree(node):
    tree = [[0] * 3 for _ in range(0, node+1)]
    for i in range(1, node//2+1):
        p = i
        l = 2 * i
        r = 2 * i + 1
        tree[p][0] = l
        if r > node:
            continue
        tree[p][1] = r
    return tree

def pre_order(n):
    global idx
    if n:
        pre_order(bin_tree[n][0])
        idx += 1
        bin_tree[idx][2] = data[idx-1]
        pre_order(bin_tree[n][1])

def post_order(n):
    if n:
        post_order(bin_tree[n][0])
        post_order(bin_tree[n][1])
        print(bin_tree[n][2])


t = sys.stdin.readlines()
data = [0] * len(t)
for i in range(0, len(t)):
    if i == len(t)-1:
        data[i] = int(t[i])
    else:
        data[i] = int(t[i].rstrip())
# 데이터 갯수를 파악한후 1 ~ N 노드까지 트리관계를 만든다. (make_bin_tree 참고)
bin_tree = make_bin_tree(len(t))
idx = 0
# 그후 중위순회를 진행하며, 노드 값에 데이터를 저장한다.
pre_order(1)
post_order(1)