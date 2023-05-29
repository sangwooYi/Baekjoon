num1 = 472
num2 = "385"

for i in range(2, -1, -1):
    cur_num = int(num2[i])
    print(num1*cur_num)
print(num1*int(num2))
