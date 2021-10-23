'''
จงเขียนโปรแกรมโดยใช้ Queue ให้สร้าง class และ method เพื่อจัดการข้อมูลโดยมีข้อมูลที่เก็บใน Queue อยู่แล้ว 
โดยตรวจสอบว่ามีข้อมูลซ้ำใน Queue หรือไม่ หลังจากดำเนินการแล้วเสร็จ และให้แสดงผลดังตัวอย่าง โดย
Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D                -> คือการนำข้อมูลด้านหน้าออก
E <value>   -> คือการนำข้อมูล value เข้าจากด้านหลัง
ตัวอย่าง
Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate

Enter Input : 1 1 1 1/E 2,E 3,D,D
Duplicate

Enter Input : 19 22 17 6 5/E 22,D
Duplicate
'''
class Queue:
    def __init__(self):
        self.item = []
    
    def enQueue(self,data):
        self.item.append(data)

    def deQueue(self):
        self.item.pop(0)

    def duplicate(self):
        Qset = set(self.item)
        if len(self.item) != len(Qset):
            return 1
        else:
            return 0

q = Queue()
x = input("Enter Input : ").split("/")
data = x[0].replace(" ","")
oder = x[1].split(",")
for i in data:
    q.enQueue(i)

for i in oder:
    temp = i.split()
    if temp[0] == 'E':
        q.enQueue(temp[1])
    elif temp[0] == 'D':
        q.deQueue()

if q.duplicate() == 1:
    print("Duplicate")
else:
    print("NO Duplicate")