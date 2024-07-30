# The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the _ numbers of the following triangle, you will get the 7th Fibonacci number:


#            1

#           1   1

#          1   2   1

#        1   3   3  _1

#      1   4  _6   4   1

#    1  _5   10  10   5   1

# _1    6   15  20   15   6   1

# Write a recursive program to calculate the Fibonacci numbers, using Pascal's triangle.

def pascal_triangle(row, col, memo):
    if col == 0 or col == row:
        return 1
    if (row, col) in memo:
        return memo[(row, col)]
    memo[(row, col)] = pascal_triangle(row - 1, col - 1, memo) + pascal_triangle(row - 1, col, memo)
    return memo[(row, col)]

def fibonacci_from_pascal(n):
    fib_sum = 0
    memo = {}
    for i in range(n + 1):
        fib_sum += pascal_triangle(i, n - i, memo)
    return fib_sum


if __name__ == "__main__":    
    # # Test the function
    # n = 7
    # print(f"The {n}th Fibonacci number using Pascal's triangle is: {fibonacci_from_pascal(n)}")
    pass
