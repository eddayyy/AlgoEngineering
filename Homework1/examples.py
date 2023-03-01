# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

def square_root(n):
    # Input: A non-negative number, n
    # Output: A floating point number, representing the square root of n 
    
    # Edge case
    if n < 0:
        return None # Return None if n is negative
    elif n == 0:
        return 0 # Returning 0 if n is 0
    else: 
        x = n # Initalize x to n 
        while True:
            y = (x + n / x) / 2 
            if abs( y - x ) < 0.0001: # 0.0001 ensures is the convergence test 
                return y
            x = y 

print(square_root(49))