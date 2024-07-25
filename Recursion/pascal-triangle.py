def pascal_triangle_value(row, col):
    # Base cases
    if col == 0 or col == row:
        return 1
    # Recursive case
    return pascal_triangle_value(row - 1, col - 1) + pascal_triangle_value(row - 1, col)

def generate_pascals_triangle_recursive(n):
    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            current_row.append(pascal_triangle_value(row, col))
        triangle.append(current_row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" " * (len(triangle) - len(row)), end="")
        for num in row:
            print(f"{num} ", end="")
        print()

# Generate and print the first 5 rows of Pascal's Triangle using recursion
rows = 5
triangle = generate_pascals_triangle_recursive(rows)
print_pascals_triangle(triangle)
