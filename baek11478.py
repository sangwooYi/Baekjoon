"""
1000 * 1000 == 100만
따라서 O(N**2) 알고리즘 가능
"""
S = input()

check_dict = {}
answer = 0
for i in range(0, len(S)):
    for j in range(i, len(S)):
        sub_str = S[i:j+1]
        if sub_str not in check_dict.keys():
            check_dict[sub_str] = 1
            answer += 1
print(answer)
