'''
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100

'''

# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzag(self, root, curr_len, goLeft):
        if root is None:
            return curr_len
        
        curr_len+=1
        if goLeft:
            # if we choose to go left -->> curr_len ++
            leftLen = self.zigzag(root.left, curr_len, not goLeft)
            # if we choose to go right -->> it is start of the new zigzag path
            rightLen = max(self.zigzag(root.right, 0, goLeft), curr_len)
        else:
            rightLen = self.zigzag(root.right, curr_len, not goLeft)
            leftLen = max(self.zigzag(root.left, 0, goLeft), curr_len)
        return max(leftLen, rightLen)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.zigzag(root.left, 0, False), self.zigzag(root.right, 0, True))