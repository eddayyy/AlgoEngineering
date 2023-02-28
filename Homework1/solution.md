# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

Q1: 

(a) for list: 
        total = total + i 

# There are a few problems with this pseudocode:
# 1. It does not initialize or define the "total" or "i" variables. 
# 2. There are no function decclarations or input output specifications 
# 3. It is unclear what datatype the list holds 
# 4. There is no specified return value for this snippet 
# 5. It isn't clear what the cases or problem this solves are so that
# fails another item in the checklist.  
#
# -------------------------------------------------------------------------
# The correct pseudocode is:                                              
                                                                        
#   Input: List "X" of integers
#   Output: Integer "total" sum of all integers in the list
    def calculate_total(list):
#       "total" will hold the sum of the integers in the lsit
        integer total = 0
#       The variable "i" is an integer element in the list given to the function
        For i IN list DO:
#           Store the sum into "total"
            total += i 
#       Return the sum of all integers in the list       
        return total
# -------------------------------------------------------------------------
#
# This new code snippet creates the function declaration with the 
# parameters, it also specifies the input, output, and datatypes of 
# the values.
#
# There is a variable declaration for "total" with a comment to 
# specify what it will hold.
#
# There is also a return value with a clear datatype that matches the # output definition

(b) "def long_division(num, denom):
        quotient = num //denom
        remainder = num % denom "

# There are a few problems with this pseudocode: 
# 1. There is no specified input / output for the function
# 2. The variables "quotient" and "remainder" are not declared
#    before being used 
# 3. There is no specified return value or datatype for it 
# -------------------------------------------------------------------------
# The correct pseudocode is
#   Input: 2 integers that arithmetic will be performed on
#          an integer "num" is the integer to be divided by the integer "denom"
#   Output: A "quotient" variable of type int that represents the division without the remainder
#           The return value 
    def long_division(num, denom):





