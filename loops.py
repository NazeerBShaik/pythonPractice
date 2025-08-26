def print_diamond(rows):
    # Upper half of the diamond
    for i in range(rows):
        # Print leading spaces
        print(" " * (rows - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

    # Lower half of the diamond
    # Start from the second-to-last row of the upper half
    for i in range(rows - 2, -1, -1):
        # Print leading spaces
        print(" " * (rows - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

# Example usage:
num_rows =5  # Adjust this value for a different size diamond
print_diamond(num_rows)