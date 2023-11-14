#Develop a program that demonstrates the use of a Python list as an array ADT
# Initializing an empty list to simulate an array
array = []

# Appending elements to the "array"
array.append(10)
array.append(20)
array.append(30)
array.append(40)

# Accessing elements by index
print("Element at index 0:", array[0])  # Output: 10
print("Element at index 2:", array[2])  # Output: 30

# Modifying elements
array[1] = 50
print("Modified array:", array)  # Output: [10, 50, 30, 40]

# Removing an element by value
array.remove(30)
print("Array after removing 30:", array)  # Output: [10, 50, 40]

# Finding the length of the array
print("Length of array:", len(array))  # Output: 3

# Checking if an element is in the array
print("Is 50 in array?", 50 in array)  # Output: True

# Iterating through the array
print("Array elements:")
for element in array:
    print(element)

