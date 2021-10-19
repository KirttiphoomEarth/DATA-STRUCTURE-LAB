# คอยนาน
# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue
# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

from collections import deque
class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


qMain = Queue()
qC1 = Queue()
qC2 = Queue()
countROW = int(0)
countCashier = int(0)
countCashier1_q = int(0)
countCashier2_q = int(0)
x = input("Enter people : ")
for i in x:
    qMain.enQueue(i)
for i in range(qMain.size()):
    if qMain.isEmpty != 0:
        countROW += 1
        countCashier1_q += 1
        if countCashier1_q == 4:
            qC1.deQueue()
            countCashier1_q = 1

        if qC1.size() < 5:
            qC1.enQueue(qMain.items[0])
        else:
            qC2.enQueue(qMain.items[0])

        if qC2.size() != 0:
            countCashier2_q += 1
        if countCashier2_q == 3:
            qC2.deQueue()
            countCashier2_q = 1

        print(countROW, end=' ')
        qMain.deQueue()
        print(qMain.items, end=' ')
        print(qC1.items, end=' ')
        print(qC2.items)
        
