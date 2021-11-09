'''จงเขียนโปรแกรม เพื่อรับข้อมูลแบบ list แล้วนำไปสร้าง BST แบบ height balanced และให้แสดงผลดังตัวอย่าง โดยให้แก้ไขใน ฟังก์ชัน list_to_bst(list_nums) เท่านั้น
***หมายเหตุ BST เป็น  Tree ที่ root โหนด มีค่ามากกว่าโหนดทางซ้าย แต่น้อยกว่าโหนดด้านขวา'''
class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None


def list_to_bst(list_nums):

    # code here

    return node


def preOrder(node):

    if not node:

        return

    print(node.val)

    preOrder(node.left)

    preOrder(node.right)


def printBST(node, level=0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)


list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)


print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)
