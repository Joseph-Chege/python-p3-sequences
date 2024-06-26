#!/usr/bin/env python3

def print_fibonacci(length):
    '''prints fibonacci sequence of length'''
    if length <= 0:
        print([])
        return
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the desired length
    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    # Adjust the length of the sequence if n is 1
    if length == 1:
        fib_sequence = [0]
    
    print(fib_sequence)
       



    pass

#Fibonnaci sequence is the two previous elements added to give the next element
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 570288