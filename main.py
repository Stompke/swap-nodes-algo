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


def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    results = []

    path = []

    def inOrderRecursive(node):
        if node.left.value > 0:
            inOrderRecursive(node.left)
        
        # print('recursive: ', node.value)
        print(node.value)
        path.append(node.value)
        if node.right.value > 0:
            inOrderRecursive(node.right)


    class BSTNode:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None


    root = BSTNode(1)
    q = deque()
    count = 0
    depth = 1

    q.appendleft(root)

    # build the tree
    while len(q) > 0:
        cur = q.pop()
        # print(cur.value)
        cur.left = BSTNode(indexes[count][0])
        if indexes[count][0] != -1:
            q.appendleft(cur.left)

        cur.right = BSTNode(indexes[count][1])
        if indexes[count][1] != -1:
            q.appendleft(cur.right)

        count += 1 

    for query in queries:

        # Show the tree
        print("\t     ", root.value)
        print("\t", "    / \\")
        print("\t  ", root.left.value,"   ", root.right.value)

        print("\t", "/  \\"," ", "/  \\")
        print("      ", root.left.left.value,"  ", root.left.right.value,root.right.left.value,"  ",root.right.right.value)

        # traverse the tree
        q = deque()
        q.appendleft(root)
        q.appendleft(False)

        # print("\n TRAVERSE TREE \n")

        # print("\t Depth: ", depth)
        while len(q) > 1:

            cur = q.pop()
            if cur == False:
                q.appendleft(False)
                depth += 1
                print("\t Depth: ", depth)

                if not depth % query:
                    print("\t\t\t It is a mulitple!")
                    print(depth, query)



                # if depth == query
                # if depth == 
            else:
                print(cur.value)

                # swap nodes
                if not depth % query:
                    print("SWAPPING AT DEPTH: ", depth)
                    cur.left, cur.right = cur.right, cur.left
                
                if cur.left.value > 0:
                    q.appendleft(cur.left)
                if cur.right.value > 0:
                    q.appendleft(cur.right)

        print('\n recursive in order sort: \n')
        inOrderRecursive(root)
        results.append(path)
        print("\t\t APPENDED TO RESULTS")
        print("Depths counted : ", depth)
        path = []
        depth = 1

        # Show the tree
        print("\t     ", root.value)
        print("\t", "    / \\")
        print("\t  ", root.left.value,"   ", root.right.value)

        print("\t", "/  \\"," ", "/  \\")
        print("      ", root.left.left.value,"  ", root.left.right.value,root.right.left.value,"  ",root.right.right.value)
        # print("      ", root.left.left.left.value,"  ",root.left.left.right.value,"  ", root.left.right.left.value,"  ", root.left.right.right.value,"  ","      ", root.right.left.left.value,"  ",root.right.left.right.value,"  ", root.right.right.left.value,"  ", root.right.right.right.value,"  ",)
    return results

        


# indices = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]

indices =  [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
queries = [2,3]

# indices = [
# [2, 3],
# [-1, -1],
# [-1, -1]
# ]
# queries = [1,1]

# indices = [
# [2, 3],
# [-1, 4],
# [-1, 5],
# [-1, -1],
# [-1, -1]
# ]
# queries = [2]

indices = [
[2, 3],
[4, -1],
[5, -1],
[6, -1],
[7, 8],
[-1, 9],
[-1, -1],
[10, 11],
[-1, -1],
[-1, -1],
[-1, -1]
]
queries = [2, 4]

print(swapNodes(indices, queries))
