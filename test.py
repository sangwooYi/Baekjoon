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

ar = [-11, 9, 5, 3, 2, 5, 7, 15, 2]

for i in range(3, -1, -1):
    print(i)