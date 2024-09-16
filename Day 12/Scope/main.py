x = 10  # Global variable

def my_function():
    x = 5                             # Local Variable
    print("Inside function, x:", x)

my_function()
print("Outside function, x:", x)
