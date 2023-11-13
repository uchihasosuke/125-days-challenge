#Day4
#Write a program to count the frequency of elements in a list.

def count_frequency(input_list):
    
    frequency_dict = {}
    
    for element in input_list:
        
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
    
    return frequency_dict

example_list = [1, 2, 2, 3, 4, 4, 4, 5]

frequency_result = count_frequency(example_list)

print(f"Original List: {example_list}")
print(f"Frequency: {frequency_result}")
