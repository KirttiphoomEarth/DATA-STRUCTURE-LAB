#  Infix to Postfix
#  ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, i):
        for x in i:
            self.items.append(x)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[-1]

x = input('Enter Infix : ')
op = {'+','-','*','/','(',')','^'}
pr = {'+':1,'-':1,'*':2,'/':2,'^':3}
s = Stack()

op1 = ""
for i in x:
    if i not in op:
        op1 += i
    elif i =='(':
        s.push(i)
    elif i ==')':
        while s.size()!= 0 and s.top() != '(':
            op1+=s.pop()
        s.pop()
    else:
        while s.size() != 0 and s.top() != '(' and pr[i] <= pr[s.top()] :
            op1 += s.pop()
        s.push(i)
while s.size() != 0:
    op1+=s.pop()
print("Postfix : "+op1)
    
