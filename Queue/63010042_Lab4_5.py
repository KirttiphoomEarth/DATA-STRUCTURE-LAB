class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def isEmpty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop(len(self.items)-1)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

Input_N, Input_M = input('Enter Input (Normal, Mirror) : ').split()
N = Stack()
M = Stack()
item = []
x = ''
combo = 0
count = 0
failed = 0
Input_M = Input_M[::-1]
for i in Input_M:
    M.push(i)
    if i == x:
        count += 1
    else:
        x = i
        count = 1
    if count == 3:
        count = 0
        item.append(M.peek())
        M.pop()
        M.pop()
        M.pop()
        if M.size() > 1:
            if M.items[-2] == M.items[-1]:
                x = M.items[-1]
                count = 2
            else:
                x = M.items[-1]
                count = 1
        elif M.size() == 1:
            x = M.items[-1]
            count = 1
length = len(item)
for i in Input_N:
    N.push(i)
    if i == x:
        count += 1
    else:
        x = i
        count = 1
    if count == 3:
        if len(item) > 0:
            y = N.peek()
            if item[0] != y:
                N.pop()
                N.push(item[0])
                item.pop(0)
                N.push(y)
                count = 1
            else:
                count = 0
                item.pop(0)
                N.pop()
                N.pop()
                failed += 1
        else:
            count = 0
            N.pop()
            N.pop()
            N.pop()
            combo += 1
            if N.size() > 1:
                if N.items[-2] == N.items[-1]:
                    x = N.items[-1]
                    count = 2
                else:
                    x = N.items[-1]
                    count = 1
            elif N.size() == 1:
                x = N.items[-1]
                count = 1

count = 0
c = []
x = ''
for i in N.items:
    c.append(i)
    if i == x:
        count += 1
    else:
        x = i
        count = 1
    if count == 3:
        count = 0
        combo += 1
        c.pop()
        c.pop()
        c.pop()
        if len(c) > 1:
            if c[-2] == c[-1]:
                x = c[-1]
                count = 2
            else:
                x = c[-1]
                count = 1
        elif len(c) == 1:
            x = c[-1]
            count = 1
N.items = c.copy()
print("NORMAL :")
print(f'{N.size()}')
if N.size() == 0:
    print('Empty', end='')
else:
    for i in range(N.size()-1, -1, -1):
        print(N.items[i], end='')
print(f'\n{combo} Explosive(s) ! ! ! (NORMAL)')
if failed > 0:
    print(f'Failed Interrupted {failed} Bomb(s)')
print("------------MIRROR------------")
print(": RORRIM")
print(f'{M.size()}')
if M.size() == 0:
    print('ytpmE')
else:
    for i in range(M.size()-1, -1, -1):
        print(M.items[i], end='')
    print()
print("(RORRIM) ! ! ! (s)evisolpxE "+str(length))
