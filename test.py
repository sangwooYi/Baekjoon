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