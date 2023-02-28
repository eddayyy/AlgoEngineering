# *********************************************************************************************************************************
# Program name: "Hamilton Problem". This program receives the input of 2 arrays, an array of distance between cities and an       *
# array of fuel at each city, it also receives an an integer. It then performs arithmetic to calculate which city would allow     *
# the user to travel in a circle to all cities without running out of fuel.                                                       *
#                                                                                                                                 * 
# Copyright (C) 2023 Eduardo Nunez & Juan Gonzalez                                                                                *
#                                                                                                                                 *
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License       *
# version 3 as published by the Free Software Foundation.                                                                         *
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied              *
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.          *
# A copy of the GNU General Public License v3 is available here:  <https://www.gnu.org/licenses/>.                                *
# *********************************************************************************************************************************
# ========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3
# 
# Authors' information
#   Author 1 name:  Eduardo Nunez
#   Author 2 name:  Juan Gonzalez 
#   Author 1 email: eduardonunez@csu.fullerton.edu
#   Author 2 email: gonzalez.juanant524@csu.fullerton.edu
#
# Program information
#   Program name: Hamilton Problem
#   Programming languages: Function Module written in Python
#   Date program began: 2023-Feb-24 0800 PDT GMT-07:00
#   Date of last update: 2023-Feb-26 1800 PDT GMT-07:00
#   Date comments upgraded: 2023-Feb-26
#   Files in this program: hamiltonProblem.py
#   Status: Finished.
#   References consulted: Geeks For Geeks, Algorithm Design in Three Acts (ADITA) By Kevin A. Wortman (Chapter 3, 4, 6), Stack Overflow, 
#                         Python Documentation: https://docs.python.org/3/library/datetime.html
# 
# Purpose
#   This program is an algorithm created to provide the user with the best city to start in  
#   techniques using lambda functions, the datetime module, iteration, etc.
# 
# This file
#   File name: hamiltonProblem.py
#   Language:  Python
# ========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
# Compiling and Linking this program and file:
#
# Step 1. Install python 3 on your machine. A tutorial for any OS can be found here https://realpython.com/installing-python/ 
#         
# Step 2. Enter the following in your linux terminal
# 
# python3 hamiltonProblem.py
# 
# ===== Begin code area ========================================================================================================
    
def find_starting_city(distances, gas, mpg):
    # Getting the length first so we don't need to keep calling it after
    # every iteration
    n = len(distances)

    # Edge case checking to make sure we are given non-empty lists and they have the same length
    # Also, if the miles per gallon is 0 
    if not distances or not gas or n != len(gas) or  mpg == 0:
        return -1

    # Introduce variable Tank that will represent the amount of fuel in the car
    tank = 0

    # Begin iteration of cities 
    for start in range(n):

        # We are reseting the tank to 0 everytime we start again in a new city
        tank = 0

        # Now we are iterating through each individual city 
        for i in range(n):
            # Calculate the index of the current city
            # Start is the beginning city for this iteration and i is the index of the current city. 
            # The modulo n is necessary because it will ensure that we always store a valid city index
            # This is to say that % n will keep our index within the bounds of the given lists
            # This step is crucial to getting the gas and distance variables necessary to update the tank
            city = (start + i) % n  

            # Updating the value of the miles left in the tank
            # We do the math in this order because we fill up on the tank before we 
            # subtract the distance
            tank += gas[city] * mpg
            tank -= distances[city]

            # This indicates that the car has ran out of fuel
            if tank < 0:
                break

        # We reached each city without running out of gas
        if tank >= 0:
            return start

    # No valid starting city found
    return -1  

city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

starting_city = find_starting_city(city_distances, fuel, mpg)

if starting_city == -1:
    print("No valid starting city found")
else:
    print("Preferred starting city:", starting_city)    







