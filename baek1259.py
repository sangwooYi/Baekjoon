import sys
sys.stdin = open("palindrome.txt")

def is_palindrome(nums):
    answer = []
    ans_list = ["no", "yes"]
    for i in range(0, len(nums)):
        now = nums[i]
        flag = True
        # 짝수면 그냥 go 홀수면 가운데 인덱스 제외 따라서 어짜피 len(now) // 2 범위까지 하면 됨
        for j in range(0, len(now) // 2):
            if now[j] != now[len(now) - 1 - j]:
                flag = False
                break
        if flag:
            answer.append(ans_list[1])
        else:
            answer.append(ans_list[0])
    return answer
                
input_numbers = []
while True:
    temp = list(map(int, input()))
    if temp[0]== 0:
        break
    input_numbers.append(temp)
    
answer = is_palindrome(input_numbers)
for i in range(0, len(answer)):
    print(answer[i])