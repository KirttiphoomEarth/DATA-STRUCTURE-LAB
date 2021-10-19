# Radix Sort (มากไปน้อย)
# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย
# โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  
# 3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

class DoublyLinkedList : #Circular Doubly linked list with dummy
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next  
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0       
    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.next
        s += str(p.data)
        return s 
    def __len__(self) :
        return self.size     
    def isEmpty(self) :
        return self.size == 0 
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    def str_reverse(self):
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.prev
        s += str(p.data)
        return s 
    def add_before(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1  
    def appending(self,data) :
        self.add_before(self.nodeAt(len(self)),data)
    def removeNode(self,q) :   
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))
x=input("Enter Input : ").split()
print('------------------------------------------------------------')
pro = DoublyLinkedList()
red = DoublyLinkedList()
rad = 1
b = 0
round=1
for i in x:
    pro.appending(i)
linkdec = []
for i in range (10):
    tempo = DoublyLinkedList()
    linkdec.append(tempo)
linkdex = []
for i in range (10):
    tempo = DoublyLinkedList()
    linkdex.append(tempo)
for i in x:
    if  linkdec[abs(int(i))//rad%10].isEmpty() :
        linkdec[abs(int(i))//rad%10].appending(i)
    else :
        isadd = 0
        for k in range(len(linkdec[abs(int(i))//rad%10])) :
            if int(linkdec[abs(int(i))//rad%10].nodeAt(k).data)<=int(i):   
                linkdec[abs(int(i))//rad%10].add_before(linkdec[abs(int(i))//rad%10].nodeAt(k),i)
                isadd =1
                break
        if isadd ==0:
            linkdec[abs(int(i))//rad%10].appending(i)
rad*=10
print('Round : '+str(round))
for i in range (10):
        print(str(i)+' : ',end='')
        if not linkdec[i].isEmpty() :
            print(linkdec[i])
        else :
            print()
print('------------------------------------------------------------')
round +=1
while(1):
    for i in range (10):
        if len(linkdec[i])==len(pro) and i==0:
            for j in range(len(linkdec[i])):
                red.appending(linkdec[i].nodeAt(j).data)
            b=1
    if b==1:
       round -=1
       break
    temp = linkdec.copy()
    current = linkdex.copy()
    for i in range (10):
        current[i] = DoublyLinkedList()
    for i in range (10):
        if not temp[i].isEmpty():
            for j in range(len(temp[i])):
                if  current[abs(int(temp[i].nodeAt(j).data))//rad%10].isEmpty() :
                    current[abs(int(temp[i].nodeAt(j).data))//rad%10].appending(temp[i].nodeAt(j).data)
                else :
                    isadd = 0
                    for k in range(len(current[abs(int(temp[i].nodeAt(j).data))//rad%10])) :
                        if int(current[abs(int(temp[i].nodeAt(j).data))//rad%10].nodeAt(k).data)<=int(temp[i].nodeAt(j).data):
                            current[abs(int(temp[i].nodeAt(j).data))//rad%10].add_before(current[abs(int(temp[i].nodeAt(j).data))//rad%10].nodeAt(k),int(temp[i].nodeAt(j).data))
                            isadd = 1
                            break
                    if isadd==0:
                        current[abs(int(temp[i].nodeAt(j).data))//rad%10].appending(temp[i].nodeAt(j).data)
    linkdec = current.copy()
    print('Round : '+str(round))
    for i in range (10):
        print(str(i)+' : ',end='')
        if not linkdec[i].isEmpty() :
            print(linkdec[i])
        else :
            print()
    for i in range (10):
        if len(linkdec[i])==len(pro) and i==0:
            for j in range(len(linkdec[i])):
                red.appending(linkdec[i].nodeAt(j).data)
            b=1
   
    if b==1:
       print('------------------------------------------------------------')
       break
    rad*=10
    round +=1
    print('------------------------------------------------------------')
print(str(round-1)+' Time(s)')
print('Before Radix Sort : ',end='')
for i in range(len(pro)-1):
    print(pro.nodeAt(i).data,end=' -> ')
print(pro.nodeAt(len(pro)-1).data)
print('After  Radix Sort : ',end='')
for i in range(len(red)-1):
    print(red.nodeAt(i).data,end=' -> ')
print(red.nodeAt(len(pro)-1).data)

