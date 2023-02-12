# writing the very first code of 2023. Usually people write hello world.
# But I am writing bye world program.
# This code is an implementation of recursive factorial.

def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n*factorial(n-1) # one extra line for debugging
        return fact

print(factorial(5))