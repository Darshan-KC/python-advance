# Write a function which implements the Pascal's triangle:


                   # 1

                # 1    1

            # 1     2     1

        # 1     3     3     1

    # 1     4     6     4     1

# 1     5     10    10     5    1


def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" " * (len(triangle) - len(row)), end="")
        for num in row:
            print(f"{num} ", end="")
        print()

# Generate and print the first 5 rows of Pascal's Triangle
rows = 5
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle)