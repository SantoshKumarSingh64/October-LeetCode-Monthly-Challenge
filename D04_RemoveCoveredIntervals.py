'''
Question Description :-
Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list.
Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.


Example 1:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:
    Input: intervals = [[1,4],[2,3]]
    Output: 1

Example 3:
    Input: intervals = [[0,10],[5,12]]
    Output: 2

Example 4:
    Input: intervals = [[3,10],[4,10],[5,11]]
    Output: 2

Example 5:
    Input: intervals = [[1,2],[1,4],[3,4]]
    Output: 1
 

Constraints:
        1 <= intervals.length <= 1000
        intervals[i].length == 2
        0 <= intervals[i][0] < intervals[i][1] <= 10^5
        All the intervals are unique.
'''
def removeCoveredIntervals(intervals):
    
    #intervals = [[1,2],[1,4],[3,4]]
    #first we sort according to first element
    intervals.sort()
    #intervals = [[1,2],[1,4],[3,4]]
    n = len(intervals)
    y = 0
    #In this loop, we sort the part of array according to second element in reverse order when first element is equal.  
    for x in range(1,n):
        if intervals[x][0] == intervals[x-1][0]:
            continue
        else:
            intervals[y:x] = sorted(intervals[y:x], key=lambda z: (z[1], -z[0]),reverse=True)
            y = x
    #intervals = [[1,4],[1,2],[3,4]]
    x = 0
    y = 1
    count = 1

    while x < n and y < n:
        if intervals[x][0] <= intervals[y][0] and intervals[x][1] >= intervals[y][1]:
            y += 1
        else:
            x = y
            y += 1
            count += 1

    #count = 1
    return count 

print(removeCoveredIntervals([[1,2],[1,4],[3,4]]))  

'''
Optimal Solution :-

def removeCoveredIntervals(intervals):
    
    n = len(intervals)
    if not n:
        return 0
        
    inter = sorted(intervals, key=lambda x: x[0]*10**6-x[1])
    ans = n
    l, r = inter[0]
    for stard, end in inter[1:]:
        if end > r:
            r = end
        elif end <= r:
            ans -= 1
        else:
            l, r = stard, end
            
    return ans
'''