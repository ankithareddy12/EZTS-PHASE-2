class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def printInorder(root):
        if root:
            printInorder(root.left)
            print(root.val,end=" ")
            printInorder(root.right)
def search(root,key):
    if root is None or root.val==key:
        return root.val
    if root.val<key:
        return search(root.right,key)

r=Node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
printInorder(r)
key=int(input())
search(r,key)
if a==key:
    print("yes")
else:
    print("no")
    
