'''จงสร้าง BST class
รับข้อมูล และแสดงผล
1. Preorder
2. Postorder
3. Inorder
4. Level order (Breadth)'''

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Queue:
    def __init__(self) :
        self.item = []
    
    def isEmpty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
    def enQueue(self, data):
        self.item.append(data)
    
    def deQueue(self):
        if not self.isEmpty():
            return self.item.pop(0)

class BTS:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
        
    def Preorder(self, node):
        if node == None:
            return ''
        s = str(node.data) + ' '\
            +self.Preorder(node.left)\
                +self.Preorder(node.right)
        return s
    
    def Postorder(self, node):
        if node == None:
            return ''
        s = self.Postorder(node.left)\
            +self.Postorder(node.right)\
                +str(node.data) + ' '
        return s
    
    def Inorder(self, node):
        if node == None:
            return ''
        s = self.Inorder(node.left)\
            +str(node.data) + ' '\
                +self.Inorder(node.right)
        return s
    
    def BFS(self):
        q = Queue()
        q.enQueue(self.root)
        s = "Level order : "
        while not q.isEmpty():
            node = q.deQueue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enQueue(node.left)
            if node.right is not None:
                q.enQueue(node.right)
        return s

   


def printBST(node, level=0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.data)
        printBST(node.left, level + 1)


T = BTS()
print(' *** Binary Search Tree ***')
inp = [int(item) for item in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
print()
print(' --- Tree traversal ---')
print(T.BFS())
print("Preorder : {0}".format(T.Preorder(T.root)))
print("Inorder : {0}".format(T.Inorder(T.root)))
print("Postorder : {0}".format(T.Postorder(T.root)))