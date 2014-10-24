#!/usr/bin/env python

from collections import deque

class Node(object):
    """
    Node object to be inserted into a Binary Search Tree.
    Has attributes data, leftChild, and rightChild
    """
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):
    def __init__(self, data=None):
        self.root = None
        self.numel = 0
        if data:
            self.root = Node(data)
            self.numel += 1

    def insert(self, data, root=None):
        if not root:
            root = self.root
        if not self.root:
            self.root = Node(data)
            self.numel += 1
            return None

        if data < root.data:
            if not root.leftChild:
                root.leftChild = Node(data)
                self.numel += 1
            else:
                self.insert(data, root.leftChild)
        elif data > root.data:
            if not root.rightChild:
                root.rightChild = Node(data)
                self.numel += 1
            else:
                self.insert(data, root.rightChild)

    def printDepth(self, N, root=None):
        if not root:
            root = self.root

        if N==0:
            print str(root.data)+' ',
            return None

        if not root.leftChild:
            return None
        self.printDepth(N-1, root.leftChild)
        if not root.rightChild:
            return None
        self.printDepth(N-1, root.rightChild)

    def levelOrderTraverse(self):
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            n = q.popleft()
            print str(n.data)+' ',
            if n.leftChild:
                q.append(n.leftChild)
            if n.rightChild:
                q.append(n.rightChild)


if __name__ == '__main__':
    bt = BinarySearchTree()
    assert bt.numel == 0
    assert bt.root == None
    bt = BinarySearchTree(5)
    assert bt.numel == 1
    assert bt.root.data == 5

    bt.insert(3)
    bt.insert(2)
    bt.insert(4)
    bt.insert(9)
    bt.insert(7)
    bt.insert(10)
    bt.printDepth(0) # should be 5
    print '\n'
    bt.printDepth(1) # should be 3 9
    print '\n'
    bt.printDepth(2) # should be 2 4 7 10
    print '\n'
    bt.levelOrderTraverse() # should be 5 3 9 2 4 7 10
    print '\n'
