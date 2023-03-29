tmp = input()

answer_char = ''
for i in range(0, len(tmp)):
    tmp_num = ord(tmp[i])
    
    ans_num = (tmp_num-3-65)%26
    answer_char += chr(ans_num+65)
print(answer_char)