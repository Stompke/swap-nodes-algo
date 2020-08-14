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

    q.appendleft(root)

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

    print("\t", root.value)
    print("\t", root.left.value)
    print("\t", root.right.right.value)

swapNodes([[2, 3], [-1, -1], [-1, -1]],1)