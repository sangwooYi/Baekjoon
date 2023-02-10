arrs = [0] * 5
max_len = 0
for i in range(0, 5):
    arrs[i] = list(input())
    max_len = max(max_len, len(arrs[i]))

answer_txt = ""

for i in range(0, max_len):
    for j in range(0, 5):
        arr = arrs[j]
        if len(arr)-1 >= i:
            answer_txt += arr[i]
print(answer_txt)