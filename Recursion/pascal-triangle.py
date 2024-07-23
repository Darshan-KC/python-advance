# Write a function which implements the Pascal's triangle:


                   # 1

                # 1    1

            # 1     2     1

        # 1     3     3     1

    # 1     4     6     4     1

# 1     5     10    10     5    1


def pascal_triangle():
    for i in range(1,7):
        print(" "*(6 - i),end="")
        print(i)
        
print("This is started")
pascal_triangle()
print("This is running")