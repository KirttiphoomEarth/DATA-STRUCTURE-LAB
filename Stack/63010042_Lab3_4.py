# Stack Calculator
# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# *************************************************
class StackCalc:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def run(self, i):
        for x in i:
            self.items.append(x)

    def getValue(self):
        stack = []
        countStr = 0
        for i in self.items:
            if i.isdigit():
                stack.append(int(i))
            elif i == '+' and len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif i == '-' and len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(x-y)
            elif i == '*' and len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif i == '/' and len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x/y))
            elif i == 'DUP':
                stack.append(stack[len(stack)-1])
            elif i == 'POP':
                stack.pop()
            else:
                countStr = 1
        if countStr == 1:
            return ("Invalid instruction: "+self.items[0]) 
        if len(stack) == 0:
            return ("0")
        elif len(stack) == 2:
            return (stack[1])
        else:
            return (stack[0])
  

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())



# items = input().split()
# stack = []
# countStr = 0
# for i in items:
#     if i.isdigit():
#         stack.append(int(i))
#     elif i == '+' and len(stack) > 1:
#         x = stack.pop()
#         y = stack.pop()
#         stack.append(x+y)
#     elif i == '-' and len(stack) > 1:
#         x = stack.pop()
#         y = stack.pop()
#         stack.append(x-y)
#     elif i == '*' and len(stack) > 1:
#         x = stack.pop()
#         y = stack.pop()
#         stack.append(x*y)
#     elif i == '/' and len(stack) > 1:
#         x = stack.pop()
#         y = stack.pop()
#         stack.append(int(x/y))
#     elif i == 'DUP':
#         stack.append(stack[len(stack)-1])
#     elif i == 'POP':
#         stack.pop()
#     else:
#         countStr = 1
        

# if countStr == 1:
#     print("Invalid instruction : "+items[0]) 
# elif len(stack) == 0:
#     print("0")
# elif len(stack) == 2:
#     print(stack[1])
# else:
#     print(stack[0])

