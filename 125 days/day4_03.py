#Day4
#Create a Python function to reverse a given list.

def reverse_list(input_list):

    reversed_list = input_list[::-1]
    return reversed_list


original_list = [1, 2, 3, 4, 5]

reversed_result = reverse_list(original_list)

print(f"Original List: {original_list}")
print(f"Reversed List: {reversed_result}")
