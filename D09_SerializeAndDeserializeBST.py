'''
Question Description :-
Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file 
or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You need to ensure that a binary search tree can be serialized to a string, and 
this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

 
Example 1:
    Input: root = [2,1,3]
    Output: [2,1,3]

Example 2:
    Input: root = []
    Output: []
 
Constraints:
    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The input tree is guaranteed to be a binary search tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return self.helper_serialize(root,"")
        
    
    def helper_serialize(self,root,string):
        if root is None:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = self.helper_serialize(root.left,string)
            string = self.helper_serialize(root.right,string)
            
        return string

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data_list = data.split(',')
        root = self.helper_deserialize(data_list)
        return root
    
    def helper_deserialize(self,lt):
        if lt[0] == 'None':
            lt.pop(0)
            return None
        else:
            root = TreeNode(lt[0])
            lt.pop(0)
            root.left = self.helper_deserialize(lt)
            root.right = self.helper_deserialize(lt)
        
        return root
            
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

'''
Optimal Solution :-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # pre-order traverse
        if root == None:
            return ""    
        return "->".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        s = collections.deque(data.split("->"))
        
        def helper(datalist:collections.deque()) -> TreeNode:
            val = datalist.popleft()
            if val == "":
                return None
            root = TreeNode(int(val), None, None)
            root.left = helper(datalist)
            root.right = helper(datalist)
            return root
        
        return helper(s)
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
'''