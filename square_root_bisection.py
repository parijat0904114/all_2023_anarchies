# Calculating a square root of a number with bisection method.
# This will help you to find a square root of an integer x without using builtin sqrt(x) or pow(x, 0.5)

def squareroot(x):
    low = 0
    high = x
    while(high-low>0.0000000000001): # change your precision here or add steps for how long you want to bisect!
        mid = (low+high)/2
        if mid*mid> x:
            high=mid
        elif mid*mid==x:
            return mid
        else:
            low = mid
    return mid

n = int(input()) # taking input
print(round(squareroot(n), 3)) # rounding to nearest 3 decimal points

# You can now have the intuition that this bisection method can be used to implement to find the nth root of
# an integer. For the cubic root, you just need to check,
# if mid*mid*mid > x
# I hope this would be helpful to understand the power of such method.