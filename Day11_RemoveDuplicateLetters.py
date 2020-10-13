'''
Question Description :-
Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:
    Input: s = "bcabc"
    Output: "abc"

Example 2:
    Input: s = "cbacdcbc"
    Output: "acdb"
 

Constraints:
    1 <= s.length <= 104
    s consists of lowercase English letters.
'''

def removeDupliceLetters(s):

    dt = {char : index for index, char in enumerate(s)}
    res = []

    for index,x in enumerate(s):
        if x not in res:
            while res and index < dt[res[-1]] and x < res[-1]:
                res.pop()
            res.append(x)
    
    return "".join(res)

print(removeDupliceLetters('bcabc'))

#This is an optimal solution.