class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL(object):

    def __init__(self):
        self.root = None
    
    def insert(self, node, data):
        if not node:
            node = Node(data)
            return node
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        
        node.height = 1 + max(self.getHeight(node.left),
                    self.getHeight(node.right))
        
        balance = self.getBalance(node)

        if balance > 1 and data < node.left.data:
            return self.RightRotate(node)
        
        if balance < -1 and data >= node.right.data:
            return self.leftRotate(node)
        
        if balance > 1 and data >= node.left.data:
           node.left = self.leftRotate(node.left)
           return self.RightRotate(node)
        
        if balance < -1 and data < node.right.data:
           node.right = self.RightRotate(node.right)
           return self.leftRotate(node)
        
        return node
    

    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 
    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        return y

    def RightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        return y
                
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input('Enter Input : ').split()
Tree = AVL()
for data in inp:
    print(f'Insert : ( {data} )')
    Tree.root = Tree.insert(Tree.root, int(data))
    Tree.printTree(Tree.root)
    print('--------------------------------------------------')