'''
Question Description :-
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.

Example 3:
    Input: nums = [0]
    Output: 0
    

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
'''

def rob(nums):
    if not nums:
        return 0
        
    if len(nums) <= 3:
        return max(nums)
        
    def helper(dp):
        dp[1] = max(dp[0],dp[1])
            
        for x in range(2,len(dp)):
            dp[x] = max(dp[x-1],dp[x] + dp[x-2])
            
        return dp[-1]
        
    p1 = helper(nums[:-1])
    p2 = helper(nums[1:])
        
    return max(p1,p2)

print(rob([1,2,3,1]))
'''
Optimal Solution :-
Upper Solution in iterative method

def rob(nums):
    
    if not nums:
        return 0
    
    n = len(nums)
    if n<=1:
        return nums[0]
    
    first = [0]*(n)
    second = [0]*(n)
    first[0] = nums[0]
    second[1] = nums[1] 
    for i in range(1,n-1):
        first[i] = max(first[i-1], nums[i]+first[i-2])
        
    for i in range(2, n):
        second[i] = max(second[i-1],nums[i]+second[i-2]) 
    
    return max(first[-2], second[-1])
'''