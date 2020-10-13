'''
Question Description :-
Sort List

Given the head of a linked list, return the list after sorting it in ascending order.
 
Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []
    

Constraints:
    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        linked_arr = []
        
        temp = head
        while temp:
            linked_arr.append([temp.val,temp])
            temp = temp.next
        
        linked_arr.sort(key = lambda x: x[0])
        
        head = linked_arr[0][1]
        temp = head
        
        for _,x in linked_arr[1:]:
            temp.next = x
            temp = temp.next
            
        temp.next = None
        return head
        
#This is an optimal solution.