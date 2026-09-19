#!/usr/bin/python3
import os
import sys

def collatz(n):
    """
    Returns the Collatz sequence starting from the given n
    """
    if n < 1:
        raise ValueError("Cannot perform Collatz sequence of non-natural numbers!!")
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in seq:
            # If the next number is already in the sequence, then we are in a cycle and won't reach 1!!
            raise RuntimeError("Oh gee, we broke the Collatz conjecture 😱")
        seq.append(n)
    return seq


if __name__ == "__main__": #This ensures that this code only runs when the file is executed directly (not when imported as a module from another file).
    n = int(input("Enter your number 😊: "))  # Heyy oyy I'm a comment
    filename = None
    while filename is None:
        temp = input("Enter the file name for the output file: ")
        if os.path.exists(temp):
            response = input(f"The file '{temp}' already exists. Do you want to overwrite it? [y/n] ")
            if response == "y":
                filename = temp
        else:
            filename = temp
    with open(filename, "w") as f:
        for i in range(1, n + 1):
            try:
                C = collatz(i)
            except RuntimeError:
                print(f"It seems like you found a number ({i}) that broke Collatz conjecture.")
                print("Please send and email to the American Mathematical Society and wait for your Nobel prize.")
                sys.exit(1)
            f.write(f"The Collatz sequence of {i} has {len(C)} terms, reaching {max(C)} on its maximum, and averaging {sum(C)/len(C):.2f}.\n")
            f.write(f"The full sequence goes like: {C}\n")
