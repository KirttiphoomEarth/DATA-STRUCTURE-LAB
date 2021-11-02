'''  Expression Tree '''
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

class BST:
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
    
    def pre_order(self, node):
        if node == None:
            return ''
        Str = str(node.data)\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return Str

    def in_order(self, node):
        if node == None:
            return ''
        Str = self.in_order(node.left)\
            + str(node.data)\
                + self.in_order(node.right)
        if node.left is not None and node.right is not None:
            Str = '(' + Str + ')'
        return Str

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    

T = BST()
s = Stack()
inp = list(input('Enter Postfix : '))
for char in inp:
    if char in '+-*/':
        temp1 = s.pop()
        temp2 = s.pop()
        s.push(Node(char, temp2, temp1))
    else:
        s.push(Node(char))

print("Tree :")
T_root = s.pop()
T.printTree(T_root)
print("--------------------------------------------------")
print("Infix :", T.in_order(T_root))
print("Prefix :", T.pre_order(T_root))