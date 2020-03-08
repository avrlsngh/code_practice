class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

    def addNode(self, n):
        if(n.val == self.val):
            if(self.left == None):
                self.left = n
            else:
                self.left.addNode(n)
        elif(n.val != self.val):
            if(self.right == None):
                self.right = n
            else:
                self.right.addNode(n)

# root node of the tree
root = None
count = 0
i = 0 
max_in = int(input("How many inputs: "))

def addValue(val):
    global root
    n = Node(val)
    if(root == None):
        root = n
    else:
        root.addNode(n)


while(True):
    if(i == max_in):
        break
    n = input("Enter the value: ")
    addValue(n)
    i = i+1


def traverse_tree(tree):
    global count
    if tree.left != None:
        count += 1
        if tree.left.left == None:
            if count % 2 == 0:
                print(str(tree.val) + " occurs odd number of time")
        else: 
            traverse_tree(tree.left)
    elif tree.left == None:
        print(str(tree.val) + " occurs odd number of time")

    if tree.right != None:
        count = 0
        traverse_tree(tree.right)

traverse_tree(root)