# MergeOrderList
# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้
# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist
# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว
# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว
# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****
# ****ห้ามสร้าง Class LinkList****

class node:
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
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    p = head
    for i in range(1,len(l)):
        p.next = node(l[i])
        p = p.next
    return head

def printList(H):
    s = ''
    p = H
    while p != None:
        s += str(p.data)+ ' '
        p = p.next
    return print(s)


def mergeOrderesList(p,q):
    if int(p.data) < int(q.data):
        temp = p
        Pnext = p.next
        Qnext = q
    else:
        temp = q
        Pnext = p
        Qnext = q.next
    head = temp
    while Pnext != None or Qnext != None:
        if Pnext != None and Qnext != None:
            if(int(Pnext.data) < int(Qnext.data)):
                temp.next = Pnext
                temp = temp.next
                Pnext = Pnext.next
            else:
                temp.next = Qnext
                temp = temp.next
                Qnext = Qnext.next
        elif Pnext != None:
            temp.next = Pnext
            temp = temp.next
            Pnext = Pnext.next
        elif Qnext != None:
            temp.next = Qnext
            temp = temp.next
            Qnext = Qnext.next
    return head
#################### FIX comand ####################   
# input only a number save in L1,L2
inp = input("Enter 2 Lists : ").split(' ')
L1 = inp[0].split(',')
L2 = inp[1].split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)