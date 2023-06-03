num1 = int(input())
num2 = input()

for i in range(2, -1, -1):
    cur_num = int(num2[i])
    print(num1*cur_num)
print(num1*int(num2))
