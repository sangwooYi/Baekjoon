import sys
sys.stdin = open("baek15719.txt")

"""
입력을 이렇게 받을 수도 있다..
"""

N = int(sys.stdin.readline().rstrip())

sum_1 = (N*(N-1))//2
sum_2 = 0

arr = sys.stdin.read()

tmp = ""
for i in range(0, len(arr)):
    if arr[i].isdigit():
        tmp += arr[i]
    elif arr[i] == " ":
        sum_2 += int(tmp)
        tmp = ""
sum_2 += int(tmp)
print(sum_2 - sum_1)


"""

import sys

def get_range_sum(final_number):
    return final_number * (final_number - 1) // 2
    

def duplicate_number(N, numbers): 
    sum_numbers = 0
    temp = ""
    for num in numbers:
        if num.isdigit():
            temp += num
        elif num == " ":
            sum_numbers += int(temp)
            temp = ""
            
    sum_numbers += int(temp)
    
    return sum_numbers - get_range_sum(N)

if __name__ == "__main__":
    N = int(input())
    numbers = sys.stdin.read()
    print(duplicate_number(N, numbers))

"""