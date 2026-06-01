# Example Python program with intentional errors for SonarQube testing

import os
import sys

def divide_numbers(a, b):
    # Potential division by zero
    return a / b  

def insecure_function():
    # Hardcoded password (security issue)
    password = "123456"
    print("Password is:", password)

def unused_function(x, y):
    # Function never used (dead code)
    return x + y

def main():
    numbers = [1, 2, 3, 4, 5]

    # Off-by-one error: accessing out-of-range index
    print("Last number:", numbers[len(numbers)])

    # Resource leak: file opened but never closed
    f = open("test.txt", "w")
    f.write("Hello World")

    # Exception not handled
    result = divide_numbers(10, 0)
    print("Result:", result)

    # Bad practice: using eval with user input
    user_input = input("Enter something: ")
    eval(user_input)

    # Unreachable code
    return
    print("This will never run")

if __name__ == "__main__":
    main()
