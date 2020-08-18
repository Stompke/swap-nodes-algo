# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

"""
UPER:
U:
    > Binary tree
    > Swap Left and Right branches when depth is a multiple of K
    > 
P:
    > Build the binary tree.
    > Traverse down 
E: 
    > CODE! 👨‍💻
R:
    > 
"""

from collections import deque




class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def swapNodes(indexes, queries):
    root = BSTNode(1)
    q = deque()
    count = 0
    depth = 1

    q.appendleft(root)

    # build the tree
    while len(q) > 0:
        cur = q.pop()
        print(cur.value)
        cur.left = BSTNode(indexes[count][0])
        if indexes[count][0] != -1:
            q.appendleft(cur.left)

        cur.right = BSTNode(indexes[count][1])
        if indexes[count][1] != -1:
            q.appendleft(cur.right)

        count += 1 


    # Show the tree
    print("\t     ", root.value)
    print("\t", "    / \\")
    print("\t  ", root.left.value,"   ", root.right.value)

    print("\t", "/  \\"," ", "/  \\")
    print("      ", root.left.left.value,"  ", root.left.right.value,root.right.left.value,"  ",root.right.right.value)

    # traverse the tree
    
    q.appendleft(root)
    q.appendleft(False)

    print("\n TRAVERSE TREE \n")

    print("\t Depth: ", depth)
    while len(q) > 1:

        cur = q.pop()
        if cur == False:
            q.appendleft(False)
            depth += 1
            print("\t Depth: ", depth)

            if not depth % queries[0]:
                print("\t\t\t It is a mulitple!")
                print(depth,queries[0])



            # if depth == queries[0]
            # if depth == 
        else:
            print(cur.value)

            # swap nodes
            if not depth % queries[0]:
                cur.left, cur.right = cur.right, cur.left
            
            if cur.left.value > 0:
                q.appendleft(cur.left)
            if cur.right.value > 0:
                q.appendleft(cur.right)
    return root

    # Show the tree
    print("\t     ", root.value)
    print("\t", "    / \\")
    print("\t  ", root.left.value,"   ", root.right.value)

    print("\t", "/  \\"," ", "/  \\")
    print("      ", root.left.left.value,"  ", root.left.right.value,root.right.left.value,"  ",root.right.right.value)

        


indices = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
queries = [2,4]

myNode = swapNodes(indices, queries)

def inOrderTraversal(rootNode):
    s = []

    s.append(rootNode.right)
    s.append(rootNode)
    s.append(rootNode.left)
    
    # while len(s) > 0:

    #     if s[-1].left:
    #         s.append(s[-1].left)
        
    #     else:
    #         removedNode = s.pop()
    #         print('removed from left: ', removedNode.value)
        
    #     if s[-1].right:
    #         s.append(s[-1])

    #     else:
    #         removedNode = s.pop()
    #         print('removed right: ', removedNode.value)

def inOrderRecursive(node):

    if node.left.value > 0:
        inOrderRecursive(node.left)
    
    print(node.value)
    if node.right.value > 0:
        inOrderRecursive(node.right)



inOrderRecursive(myNode)