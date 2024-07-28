# The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the _ numbers of the following triangle, you will get the 7th Fibonacci number:


#            1

#           1   1

#          1   2   1

#        1   3   3  _1

#      1   4  _6   4   1

#    1  _5   10  10   5   1

# _1    6   15  20   15   6   1

# Write a recursive program to calculate the Fibonacci numbers, using Pascal's triangle.

def pascal_triangle(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)