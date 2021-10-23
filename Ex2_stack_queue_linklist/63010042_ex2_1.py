'''
จงสร้างโครงสร้างข้อมูล Stack ที่มี method ดังต่อไปนี้ 
__str__ สำหรบแสดงข้อมูลที่อยู่ใน stack
push(data) สำหรับเก็บข้อมูล data   
pop() สำหรับนำข้อมูลออก
isEmpty() สำหรับตรวจสอบว่า stack ว่างไหม ถ้าว่าง ให้เป็น True
size() สำหรับแสดงขนาดของ stack ว่ามีข้อมูลกี่ตัว
peek() สำหรับแสดงค่าข้อมูลที่อยู่ที่อยู่บนสุด
bottom() สำหรับแสดงค่าข้อมูลที่อยู่ล่างสุด
โดยเมื่อป้อน 1 แล้วให้ทำงานคำสั่งต่อไปนี้ 
'''

class Stack:
    def __init__(self):
        self.item = []

    def __str__(self):
        s = 'Data in Stack is : '
        for i in self.item:
            s += str(i) +' '
        return s

    def push(self,data):
        self.item.append(data)

    def pop(self):
        self.item.pop()
    
    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0] 

s1 = Stack()
inp = input("Enter choice : ")
if inp == '1':
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif inp == '2':
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif inp == '3':
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())