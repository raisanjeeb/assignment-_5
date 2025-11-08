import sys  # Import the built-in sys module

# Check if the user has provided at least two command-line arguments
if len(sys.argv) != 3:
    # Exit the program with an error message if not enough arguments
    sys.exit("Error: Please provide exactly two numbers as command-line arguments.")

# Convert command-line arguments to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Add the two numbers
total = num1 + num2

# Print the result
print("The sum is:", total)
