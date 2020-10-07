'''
Question Description :- 
Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
        rotate 1 steps to the right: 2->0->1->NULL
        rotate 2 steps to the right: 1->2->0->NULL
        rotate 3 steps to the right: 0->1->2->NULL
        rotate 4 steps to the right: 2->0->1->NULL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        n = len(arr)
        if n == 0:
            return 
        k =  k%n
        
        def leftrotate():
            temp = arr.pop()
            arr.insert(0,temp)
            
        for _ in range(k):
            leftrotate()
            
        temp = arr[0]
        for x in arr[1:]:
            temp.next = x
            temp = temp.next
            
        temp.next = None
        
        return arr[0]

'''
Optimal Solution :-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        temp = head
        n_count=1
        while temp.next!=None:
            n_count+=1
            temp=temp.next
        k = n_count-k%n_count
        if k == 0:
            return head
        temp.next = head
        temp=head
        for _ in range(k-1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
        
'''