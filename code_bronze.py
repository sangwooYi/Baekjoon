# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
# \ 출력은 \\로 한다!
#  " 나 \ 같은애를 출려하고싶으면 \"   \\ 이런식으로 써야만한다!


print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")


N = int(input())
nums = list(map(int, input().split()))
min_num = nums[0]
max_num = nums[0]
# 정렬해서 하는것보다 이게 훨씬 시간복잡도 짧다
for i in range(0, N):
    if min_num >= nums[i]:
        min_num = nums[i]
    if max_num <= nums[i]:
        max_num = nums[i]
print(f"{min_num} {max_num}")


A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

N, X = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
for i in range(0, len(nums)):
    if nums[i] < X:
        answer.append(nums[i])
for i in range(0, len(answer)):
    if i == len(answer)-1:
        print(answer[i])
    else:
        print(answer[i], end=" ")

N = int(input())
for i in range(0, N):
    A, B = map(int, input().split())
    print(A+B)

