'''
Question Description :-
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 
Example 1:
    Input: root = [3,9,20,null,null,15,7]
                        3
                    /   \
                    9      20
                        /  \
                        15   7 
    Output: 2

Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5
 

Constraints:
    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
            
        q = []
        q.append({'node':root, 'depth':1})

        #level order traversal approach
        while len(q) > 0:

            queueItem = q.pop(0)
            node = queueItem['node']
            depth = queueItem['depth']

            if node.left is None and node.right is None:
                return depth

            if node.left:
                q.append({'node':node.left, 'depth':depth+1})

            if node.right:
                q.append({'node':node.right, 'depth':depth+1})



