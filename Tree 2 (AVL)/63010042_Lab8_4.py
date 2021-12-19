class Node:
    
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
       
    
    def __str__(self):
        return str(self.data) + ' ' +str(self.pos)

class Tree:

    def __init__(self):
        self.root = []
    
    def insert(self, data, pos):
        self.root.append(Node(data, pos))
    
    def left(self, z):
        if (z.data * 2)+1 < len(self.root):
            return self.root[(z.data*2)+1]
        else:
            return None
        
    def right(self, z):
        if (z.data * 2)+2 < len(self.root):
            return self.root[(z.data*2)+2]
        else:
            return None    
    
def findSum(node, x):
    lis = []
    s = 0
    temp = node.root[x]
    lis.append(temp)
    while len(lis) > 0:
        t = lis[0]
        lis.pop(0)
        if node.left(t) != None:
            lis.append(node.left(t))
        s += t.pos
        if node.right(t) != None:
            lis.append(node.right(t))
    return s

    
def power(node, a, b):
    pa = findSum(node, a)
    pb = findSum(node, b)
    if pa < pb:
        return str(a) + '<' + str(b)
    elif pa > pb:
        return str(a) + '>' + str(b)
    elif pa == pb:
        return str(a) + '=' + str(b)       
   
T = Tree() 
a, b = input('Enter Input : ').split('/')
data = [i for i in b.split(',')]
inp = [int(i) for i in a.split()]
for i in range(len(inp)):
    r = T.insert(i, inp[i])
print(str(findSum(T, 0)))
for i in data:
    t = [j for j in i.split()]
    print(power(T,int(t[0]),int(t[1])))