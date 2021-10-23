'''
จงเขียนโปรแกรมแบ่งการเรียงลำดับจากตัวเลขที่ป้อนเข้าไป โดยให้ส่วนต้นเริ่มที่เลข 0 ต่อด้วยส่วนท้ายของลำดับที่เหลือ ดังตัวอย่าง
การเขียนโปรแกรมนี้ให้การเขียนโปรแกรมด้วย singly linked list
ตัวอย่าง
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1

Enter Input : 1 0
Before : 1 <- 0
After : 0 <- 1

Enter Input : 0 1 2 3 4 5 6 7 8 9
Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9

Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3
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

    def ReOder(self):
        if self.head.data == '0':
            return
        elif self.tail.data == '0':
            p = self.head
            n = self.head.next
            while p.next != None:


            
x = input("Enter numbers : ").split()
ll = LinkedList()
for i in x:
    ll.append(i)

print(ll)
# ll.reverse()
ll.ReOder()
print(ll)