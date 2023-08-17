#!/usr/bin/env python3

# def print_fibonacci(length):
#     # print(print_fibonacci([])) 
#     # length = 9
#     pass
# fibonacci= []
# len = length
# print(length(fibonacci))
    
#     # print(print_fibonacci(0))


def print_fibonacci(length):
    # fibonacci_sequence = []

    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_sequence.append(
                        fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    print(fibonacci_sequence)


# Testing the function with different lengths
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)

    

        # for num in fibonacci_sequence:
            # print(num)

# Testing the function with different lengths
# print_fibonacci(0)
# print()
# print_fibonacci(1)
# print()
# print_fibonacci(2)
# print()
# print_fibonacci(10)

    

    # print(fibonacci_sequence)

# Call the function to print the Fibonacci sequence up to length 10
# print_fibonacci(10)

