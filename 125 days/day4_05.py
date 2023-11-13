#Day4
#Develop a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
    
    unique_list = list(set(input_list))
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 4, 5]

unique_result = remove_duplicates(original_list)

print(f"Original List: {original_list}")
print(f"List without Duplicates: {unique_result}")
