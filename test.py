# class Queue:

#     def __init__(self, capacity):
#         # 파이선에서 클래스 필드 선언 및 초기화법
#         self.max = capacity
#         self.front = 0
#         self.rear = 0
#         self.data = 0
#         self.queue = [0] * self.max

#     def enqueue(self, x):
#         if self.data >= self.max:
#             return -1
#         self.queue[self.rear] = x
#         self.data += 1
#         self.rear += 1
#         if self.rear == self.max:
#             self.rear = 0
#         return x

#     def dequeue(self):
#         now = self.queue[self.front]
#         self.data -= 1
#         self.front += 1
#         if self.front == self.max:
#             self.front = 0
#         return now

#     def is_full(self):
#         return self.data >= self.max



# que = Queue(100)
# que.enqueue(3)
# que.enqueue(5)
# print(que.dequeue())
# print(que.dequeue())
# a = [5, 1, 2, 4, 3]

# b = a
# b.sort()
# print(a)

# 여기엔 인덱스 값이 들어감
def swap(a, idx1, idx2):
    temp = a[idx1]
    a[idx1] = a[idx2]
    a[idx2] = temp


def quickSort(arr, left, right):
    pl = left
    pr = right
    pv = arr[(pl + pr) // 2]
    while pl <= pr:
        while arr[pl] < pv:
            pl += 1
        while arr[pr] > pv:
            pr -= 1
        # 아직 범위가 유효할때만
        if (pl <= pr):
            # 바꾸고나서 한번 더이 동
            swap(arr, pl, pr)
            pl += 1
            pr -= 1
    # 위에서 while문 벗어났으면 이미 pl > pr 인 상황
    if left < pr:
        quickSort(arr, left, pr)
    if pl < right:
        quickSort(arr, pl, right)


class Stack:
    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.data = 0
        self.ptr = 0

    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.data += 1
        self.ptr += 1
        return x

    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def is_empty(self):
        return self.data <= 0


"""
이분 탐색에서, 단순히 찾는것 외에
lower bound upper bound 자체도 구현이 가능해야한다.
"""

# 그냥 특정 값을 찾는 경우
def binarySearch(arr, key):
    pl = arr[0]
    pr = arr[len(arr) - 1]
    while pl <= pr:
        pc = (pl + pr) // 2
        if arr[pc] == key:
            return pc
        elif arr[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1

def upperBound(arr, key):
    pl = arr[0]
    pr = arr[len(arr) - 1]
    # upperBound, lowerBound는 pl == pr이 같아지는 순간 종료한다.
    while pl < pr:
        pc = (pl + pr) // 2
        # upperBound의 경우는 key값에 비해 현재 pc 위치의 값이 큰 경우에만 pr 줄인다. 
        if arr[pc] > key:
            pr = pc
        # arr[pc] == key 인 경우에도 pl을 움직인다.
        else:
            pl = pc + 1 
    return pl

# arr[pc] == key일때 pr 을 움직이는게 lower bound
# arr[pc] == key일때 pl을 움직이는게 upper bound
def lowerBound(arr, key):
    pl = arr[0]
    pr = arr[len(arr) - 1]
    while pl < pr:
        pc = (pl + pr) // 2
        if arr[pc] >= key:
            pr = pc
        else:
            pl = pc + 1

# 위와 같이 코드 짜게 되면
# lower bound 의 경우는 정말 해당 값이 존재하는 가장 낮은 인덱스값에서 멈추고
# upper bound는 해당 값지 존재하는 가장 높은 인덱스 바로 다음 인덱스에서 멈춘다!
# 위와 같이 코드 짜는거 명심, upperbound는 실제 값 자체가 필요하면 인데스 1 빼주는거 

# 근데 존재하지 않는 경우가지 따져야 하므로 그냥 upperBound의 인덱스 - lowerBound의 인덱스로 간다.
# 값이 없는 경우는 upperbound 인덱스 == lowerbound인덱스 가 되므로! (직접 그려보면 된다.)
# def find_max(a, b, c):
#     if a >= b:
#         if a >= c:
#             return a
#         return c
#     else:
#         if b >= c:
#             return b
#         return c
# # 파이선 for문은 아래와같이 작성하면 에러발생은 안하고 그냥 동작을 안함
# for i in range(4, 2):
#     print(i)

# A ~ Z 65 부터 90,  a ~ z  97 부터 122
# alph = input()
# check = [-1] * 26
# for i in range(0, len(alph)):
#     conv = ord(alph[i]) - 97
#     # 아직 체크가 안된 애면
#     if check[conv] == -1:
#         check[conv] = i
# for i in range(0, len(check)):
#     if i == len(check)-1:
#         print(check[i])
#     else:
#         print(check[i], end=" ")


# def operL(num):   
#     res = (num % 1000) * 10 + (num // 1000)
#     return res

# def operR(num):
#     res = (num % 10) * 1000 + (num // 10)
#     return res

# a = 1410

# print(operL(a), operR(a))

# def GCD(num1, num2) :
#     if num2 == 0:
#         return num1
#     else : 
#         return GCD(num2, num1 % num2)

# print(GCD(20, 7))

# sum = 0
# N = int(input())
# nums = input()
# for i in range(0, N):
#     sum += int(nums[i])
# print(sum)

def check_pelindrome(arr):
    for i in range(0, len(arr)):
        if arr[i] != arr[len(arr)-1-i]:
            return False
    return True
