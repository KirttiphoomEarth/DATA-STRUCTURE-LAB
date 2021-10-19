# Canteen
# โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน 
# ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
# Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear
# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# E < id >  ->   เป็นการนำพนักงานเข้า Queue
# D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty
# อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  
# และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

from collections import deque
from os import path
from typing import Counter
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
    
    def clean(self):
        self.items = []
    
    def lastQ(self):
        if self.isEmpty():
            return []
        else:
            return self.items[-1]

    def Num0(self):
        return self.items[0]


q = Queue()
x = input("Enter Input : ").split("/")
listt01 = x[0].split(",")
listt02 = x[1].split(",")
listtS = [[]]
sublist = []

noQ = int(0)
inQ = int(0)
max = int(0)
check = int(0)
count = int(0)

for i in listt01:
    temp = i.split()
    max = int(temp[0])
    
for i in range(max):
    for j in listt01:
        temp = j.split()
        if int(temp[0]) == i+1:
            sublist.append(temp[1])
    listtS.append(sublist)
    sublist = []

for i in listt02:
    temp = i.split()
    if temp[0] == 'D':
        if q.size() == 0:
            print("Empty")
        else :
            for i in q.items:
                t = i.split()
                #print(t)
                print(t[0])
                break
            q.deQueue()
    elif temp[0] == 'E':
        data = temp[1]
        tempCheck = []
        found = 0
        pn = 0
        for j in range(len(listtS)):
            if data in listtS[j]:
                #tempData =  listtS[j].split()
                data+=' '+str(j)
                pn = j
                #print(data)
                #print(pn)
        if q.size() > 1:
            for j in range(q.size()-1):
                c = q.items[j].split()
                cn = q.items[j+1].split()
                #print(c)
                #print(cn)
                if pn == int(c[1]) and pn != int(cn[1]):
                    tempCheck.append(q.items[j])
                    tempCheck.append(data)
                    found = 1
                else :
                    tempCheck.append(q.items[j])
            tempCheck.append(q.items[q.size()-1])
            if found == 0 :
                tempCheck.append(data)
        else :
            tempCheck = q.items.copy()
            tempCheck.append(data)
        q.items = tempCheck.copy()

        
# print(q.items)
# print(listtS)
# 1 101,1 102,2 201,2 202,3 301,3 302,4 405/5
# 1 41,1 42,1 43,2 201,2 202,2 203,3 301/D,E 41,E 201,E 42,D,D,E 43
# 1 101,1 102,1 103,2 202,2 203,3 301/E 101,E 102,E 202,E 103