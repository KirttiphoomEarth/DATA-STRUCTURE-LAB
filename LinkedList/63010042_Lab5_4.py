# VIM Text Editor
# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ 
# Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ 
# Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย 
# กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย 
# โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor
# ***** อธิบาย Input 5 แบบ *****
# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
# 2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
# 3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
# 4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
# 5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = Node('|')
        self.size = 1

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def insrt(self, data):
        newNode = Node(data)
        self.size += 1

        p = self.head
        while p.data != '|':
            p = p.next
        newNode.next = p

        if p.previous != None:
            p.previous.next = newNode
        newNode.previous = p.previous
        if p.previous == None:
            self.head = newNode
        p.previous = newNode

    def Left(self):
        p = self.head
        if p.data == '|':
            return
        while p.next.data != '|':
            p = p.next
        node = p.next

        if p.previous != None:
            p.previous.next = node
        p.next = node.next
        node.next = p
        node.previous = p.previous
        if p.previous != None:
            p.previous = node

        if p.next == None:
            self.tail = p
        if node.previous == None:
            self.head = node

    def Right(self):
        p = self.head
        if self.tail.data == '|':
            return

        while p.data != '|':
            p = p.next
        node = p.next
        if p.previous != None:
            p.previous.next = node
        else:
            self.head = node
        p.next = node.next
        if node.next != None:
            node.next.previous = p
        else:
            self.tail = p
        node.next = p
        node.previous = p.previous
        p.previous = node

    def D(self):
        if self.tail.data == '|' or self.size < 2:
            return

        p = self.head
        while p.data != '|':
            p = p.next
        node = p.next
        p.next = node.next
        if node.next != None:
            node.next.previous = p
        else:
            self.tail = p

    def B(self):
        if self.head.data == '|':
            return

        p = self.head
        while p.next.data != '|':
            p = p.next
        node = p.next
        node.previous = p.previous
        if p.previous != None:
            node.previous.next = node
        else:
            self.head = node


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    temp = i.split()
    # print(temp)
    if temp[0] == 'I':
        L.insrt(temp[1])
    elif temp[0] == 'L':
        L.Left()
    elif temp[0] == 'R':
        L.Right()
    elif temp[0] == 'B':
        L.B()
    elif temp[0] == 'D':
        L.D()
print(L)
