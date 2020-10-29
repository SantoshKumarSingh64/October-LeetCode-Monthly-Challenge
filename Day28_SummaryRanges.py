'''
Question Description :-
Summary Ranges

You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
 

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
                            [0,2] --> "0->2"
                            [4,5] --> "4->5"
                            [7,7] --> "7"
        

Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
                            [0,0] --> "0"
                            [2,4] --> "2->4"
                            [6,6] --> "6"
                            [8,9] --> "8->9"

Example 3:
    Input: nums = []
    Output: []

Example 4:
    Input: nums = [-1]
    Output: ["-1"]

Example 5:
    Input: nums = [0]
    Output: ["0"]
 

Constraints:
    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
'''
def summaryRanges(nums):
    
    if not nums:
        return []

    ans = []
    start = nums[0]
    end = nums[0]
    count = 1
    for x in nums[1:]:
        if (x-start) == count:
            end = x
            count += 1
        else:
            if count != 1:
                ans.append(str(start)+'->'+str(end))
            else:
                ans.append(str(start))
            start = x
            end = x
            count = 1
    if count != 1:
        ans.append(str(start)+'->'+str(end))
    else:
        ans.append(str(start))
    return ans

print(summaryRanges([0,2,3,4,6,8,9]))
#This solution of O(n), so it also a optimal solution.