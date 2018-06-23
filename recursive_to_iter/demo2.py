# -*- coding: utf-8 -*-

"""
 二叉树
"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(pRoot):
    if pRoot == None:
        return None
    inorder(pRoot.left)
    print(pRoot.val)
    inorder(pRoot.right)

# 非递归
def inorder_iter(pRoot):
    if pRoot == None:
        return None
    stack = []
    p = pRoot
    while p != None or len(stack) > 0:
        while p:
            stack.append(p)
            p = p.left
        p = stack.pop()
        print(p.val)
        p = p.right

if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    inorder(tree)
    print("---")
    inorder_iter(tree)    
