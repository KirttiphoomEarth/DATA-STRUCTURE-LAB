# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด
# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด
# 2. วงเล็บปิดเกิน
# 3. วงเล็บเปิดเกิน
# แล้วให้แสดงผลตามตัวอย่าง

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
listChack = []
notMatc = 0
unmatch = 0
openCheck = int(0)
closeCheck = int(0)
string = input("Enter expresion : ")
stack = []
for i in string:
    if i in open_list:
            stack.append(i)
            openCheck += 1
    elif i in close_list:
            closeCheck += 1
            pos = close_list.index(i)
            if ((len(stack) > 0) and+
            
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                if closeCheck == 1:
                    unmatch = 1
                else:
                    notMatc = 1

if openCheck != 0 and unmatch == 1:
    print(string+" Unmatch open-close")
elif openCheck < closeCheck:
    print(string+" close paren excess")
elif openCheck != 0 and closeCheck == 0:
    print(string+" open paren excess   "+str(openCheck)+" : "+string)
elif len(stack) == 1:
    print(string+" open paren excess   "+str(len(stack))+" : "+stack[0])
else:
    print(string+" MATCH")
  

  

