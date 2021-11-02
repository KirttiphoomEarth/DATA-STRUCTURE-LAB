'''  หาค่า Below '''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.less = []

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

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    v = ''
    def less_than(self, node, n):
        
        if node == None:
            return 
        if node.left!=None:
            self.less_than(node.left, n)
        if int(node.data) < n:
            self.v+=str(node.data)+' '
          #print(str(node.data),end=' ')
        if node.right!=None:
            self.less_than(node.right, n)
        if self.v =='':
            return "Not have"
        else :
            return self.v


T = BST()
inp, k = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print("Below {0} : ".format(k),end='')
below = T.less_than(root, int(k))
print(below)

