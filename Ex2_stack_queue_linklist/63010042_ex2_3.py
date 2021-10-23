'''
จาก class LinkedList ในข้อ 2 จงเขียน method reverse เพิ่มเข้าไปใน class LinkedList เพื่อทำหน้าที่กลับลำดับของโหนดต่าง ๆ ในลิสต์ 
โดยให้โปรแกรมรับค่าข้อมูลจากผู้ใช้ แล้วแสดงค่าข้อมูลใน LinkList แบบเรียงตามลำดับที่รับข้อมูล และ แบบย้อนกลับ
แบบปกติ
head-->a-->b-->c-->d
แบบย้อนกลับ
head-->d-->c-->b-->a
'''
class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def reverse(self):
        previous = None
        p = self.head
        while p != None:
           next = p.next
           p.next = previous
           previous = p
           p = next
        self.head = previous

x = input("Enter numbers : ").split()
ll = LinkedList()
for i in x:
    ll.append(i)
print("Linkedlist Before Reverse")
print(ll)
print("Linkedlist After Reverse")
ll.reverse()
print(ll)