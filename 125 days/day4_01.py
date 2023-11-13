#Day-4
#Write a Python program to count the number of vowels in a string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_string = input("Enter a string: ")

result = count_vowels(input_string)

print(f"The number of vowels in '{input_string}' is: {result}")

