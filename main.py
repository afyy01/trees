class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#manually add the nodes
root = Tree(1)
root.left = Tree(2)
root.right =Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)

#preOrder => root, left subtree , right subtree
def preorder_traversal(node):
    if node:
        print(node.data, end= " - ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

#inorder => left subtree, root, right subtree
def inorder_traversal(node):
    if node:

        preorder_traversal(node.left)
        print(node.data, end= " - ")
        preorder_traversal(node.right)

#post order =>left subtree, right subtree, root
def postorder_traversal(node):
    if node:

        preorder_traversal(node.left)
        preorder_traversal(node.right)
        print(node.data, end= " - ")

print("PreOrder transversal is: ")
preorder_traversal(root)


print("\n InOrder transversal is: ")
inorder_traversal(root)

print("\n PostOrder transversal is: ")
postorder_traversal(root)



