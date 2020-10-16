'''
Question Description :-
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
    Output: false

Example 3:
    Input: matrix = [], target = 0
    Output: false
 

Constraints:
    m == matrix.length
    n == matrix[i].length
    0 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
'''
def searchMatrix(matrix, target):
    
    for x in matrix:
        if target in x:
            return True
    return False

#This is an optimal solution.