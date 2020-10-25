'''
Question Description :-
132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 
Example 1:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.

Example 2:
    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
    Input: nums = [-1,3,2,0]
    Output: true
    Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:
    n == nums.length
    1 <= n <= 104
    -109 <= nums[i] <= 109
'''
def find132pattern(nums):

    min_list = [0] * len(nums)
    min_list[0] = nums[0]
    stack = []
    for x in range(1,len(nums)):
        min_list[x] = min(nums[x-1],min_list[x-1])
    
    for j in range(len(nums)-1,-1,-1):
        if nums[j] > min_list[j]:
            while stack and stack[-1] <= min_list[j]:
                stack.pop()

            if stack and stack[-1] < nums[j]:
                return True

            stack.append(nums[j])

    return False

print(find132pattern([6,12,3,4,6,11,20]))
#This is an optimal solution.