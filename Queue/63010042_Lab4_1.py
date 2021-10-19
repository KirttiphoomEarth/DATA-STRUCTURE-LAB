# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา
# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE
# D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1
# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

from collections import deque
class Queue:
    def __init__(self):
        self.items = []
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

q = Queue()
qAns = Queue()
Dcount = int(0)
Ecount = int(0)
x = input("Enter Input : ").split(",")
for i in range(len(x)):
    q.enQueue(x[i])
for i in q.items:
    tempo = i.split()
    if tempo[0] == 'E':
        Ecount += 1
        qAns.enQueue(tempo[1])
        print(qAns.size())
    elif tempo[0] == 'D':
        Dcount += 1;
        if qAns.isEmpty() == 1:
            print("-1")
        else:
            print(qAns.deQueue()+" 0")

for i in qAns.items:
    print(i,end=' ')
if Dcount >= Ecount and q.items[-1] == 'D':
    print("Empty")
