# ซอยตัน
# ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ 
# แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack 
# เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output
# การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ 
# รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย 
# โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4
# ***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***
# *** สามารถสร้างได้มากกว่า 1 stack ***

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, i):
        for x in i:
            self.items.append(x)
    def pop(self,i = None):
        if i == 0:
            return self.items.pop(0)
        else:
            return self.items.pop()
    def remove(self,i):
        return self.items.remove(i)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

sIn = Stack()
sMain = Stack()
cou = int(0)
print("******** Parking Lot ********")
x = input("Enter max of car,car in soi,operation : ").split()
for i in x[1]:
    sIn.push(i)
sMain.push([ele for ele in sIn.items if ele.strip(',')])

if x[2] == 'arrive' and x[3] in sMain.items:
    print("car "+x[3]+" already in soi")
elif x[2] == 'arrive' and x[1] == '0':
    sMain.pop()
    sMain.push(x[3])
    print("car "+x[3]+" arrive! : "+"Add Car "+x[3])
elif x[2] == 'arrive' and sMain.size() < int(x[0]):
    sMain.push(x[3])
    print("car "+x[3]+" arrive! : "+"Add Car "+x[3])
elif x[2] == 'arrive':
    print("car "+x[3]+" cannot arrive : "+"Soi Full")

if x[2] == 'depart' and x[1] == '0' :
    sMain.pop()
    print("car "+x[3]+" cannot depart : Soi Empty")
elif x[2] == 'depart' and x[3] not in sMain.items:
    print("car "+x[3]+" cannot depart : Dont Have Car "+x[3])
elif x[2] == 'depart' and x[3] != sMain.items[0]:
    sMain.remove(x[3])
    print("car "+x[3]+" depart ! : Car "+x[3]+" was remove")
elif x[2] == 'depart':
    sMain.pop(0)
    print("car "+x[3]+" depart ! : Car "+x[3]+" was remove")

print("[",end='')

for i in sMain.items:
    cou += 1
    if cou <= sMain.size()-1:
        print(i+", ",end='')
    elif cou == sMain.size():
        print(i,end='')

print("]")
