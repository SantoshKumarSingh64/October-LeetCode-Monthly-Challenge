'''
Question Description :-
Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 
Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
 

Constraints:
    0 <= s.length <= 105
    s[i] is 'A', 'C', 'G', or 'T'.
'''
def findRepeatedDnaSequences(s):
    
    if len(s) <= 10:
        return []
    ans = []
    dt = {}
    for x in range(0,len(s)-9):
        temp = s[x:x+10]
        if temp in dt:
            if dt[temp] == 1:
                ans.append(temp)
            dt[temp] += 1
            
        else:
            dt[temp] = 1

    return ans

print(findRepeatedDnaSequences("AAAAAAAAAAA"))
#This is an optimal solution.