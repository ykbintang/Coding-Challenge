def print_cube(input_number):
    for num in range(1, input_number + 1):
        cube = num**3
        print(f"Current Number is : {num} and the cube is {cube}")


# Given input
input_number = 6

# Print the cubes of numbers from 1 to the given input_number
print_cube(input_number)
