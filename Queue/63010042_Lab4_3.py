# code with queue
# รับ string มาเข้าคิวหา secret code โดยรับ input คือ
# code เป็น string ยาว
# hint คือตัวแรกของรหัสที่ถูกต้อง

# **คำใบ้**
# ascii ของ "f" มีค่า = 102
# ascii ของ "g" มีค่า = 103
# ascii ของ "h" มีค่า = 104
# ascii ของ "i" มีค่า = 105
# ascii ของ "j" มีค่า = 106

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
x = input("Enter code,hint : ").split(",")
cnum = ord(x[1]) - ord(x[0][0])
for i in x[0]:
    temp = ord(i)
    q.enQueue(chr(temp+cnum))
    print(q.items)
