import sys
sys.stdin = open("baek17219.txt")


N, M = map(int, sys.stdin.readline().split())

site_dict = {}
for i in range(0, N):
    site, pw = sys.stdin.readline().split()
    site_dict[site] = pw
for i in range(0, M):
    search = sys.stdin.readline().rstrip()
    print(site_dict[search])