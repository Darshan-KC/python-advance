# Write a recursive Python function that returns the sum of the first n integers. (Hint: The function will be similiar to the factorial function!)

def sum(n:int) -> int:
    """
        Recursive function to find the sum of first n integers
        
        Parameters
        n (int): nth number to calculate sum
    """
    if n == 0:
        return 0
    return sum(n - 1) + n

def main() -> None:
    """
        Main function
    """
    try:
        n = int(input("Enter a number : "))
        if n < 0:
            print("Number cannot be less than 0")
            exit()
        print("The sum of first {} integers is {}".format(n,sum(n)))
    except:
        print("Enter a valid number")
        
if __name__ == "__main__":
    main()