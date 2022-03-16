numbers = [2, 4, 6, 8, 10]
print("List of numbers:")
print(numbers)
print("\nSquare of every number of the provided list:")
square_numbers = list(map(lambda x: x ** 2, numbers))
print(square_numbers)
print("\nCube of every number of the provided list:")
cube_numbers = list(map(lambda x: x ** 3, numbers))
print(cube_numbers)