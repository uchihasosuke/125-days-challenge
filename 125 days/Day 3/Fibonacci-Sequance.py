#Write a program to print the fibonacci sequance up to N terms

def fibonacci_sequence(n):
    fibonacci = [0, 1]
    
    while len(fibonacci) < n:
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)
    
    return fibonacci[:n]

# Get user input for the number of terms (N)
num_terms = int(input("Enter the number of terms (N) for the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence up to N terms
fibonacci_result = fibonacci_sequence(num_terms)
print(f"The Fibonacci sequence up to {num_terms} terms is: {fibonacci_result}")
