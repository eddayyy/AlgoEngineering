# Authors: Eduardo Nunez | Juan Gonzalez
# Authors email: eduardonunez@csu.fullerton.edu 
#                gonzalez.juanant524@csu.fullerton.edu

import json # Import the json module for loading data from a file
import heapq # Import the heapq module for heap operations (not used in this code)

# Define a function that reads input from a file in JSON format
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        arrays = json.load(file)
    return arrays

# Define a function that merges sorted subarrays into a single sorted array (Version 1)
def merge_sort_subarrays_v1(array):
    # Initialize an empty list for the merged array and a list of subarray indices
    merged_array = []
    subarray_indices = [0] * len(array)
    
    # Loop until all subarrays have been exhausted
    while True:
        # Create a list of tuples, where each tuple contains the smallest item in a subarray and the index of that subarray
        smallest_items = []
        for i, subarray in enumerate(array):
            if subarray_indices[i] < len(subarray):
                smallest_items.append((subarray[subarray_indices[i]], i))
        
        # If there are no more smallest items, break out of the loop
        if not smallest_items:
            break
        
        # Find the smallest item and its index in the smallest_items list, append it to the merged array, and increment the corresponding subarray index
        min_item, min_index = min(smallest_items)
        merged_array.append(min_item)
        subarray_indices[min_index] += 1
    
    # Return the merged array
    return merged_array

# Set the filename for the input file
input_filename = "in2C.txt"

# Read the input arrays from the file using the read_input_from_file() function
input_arrays = read_input_from_file(input_filename)

# Apply Version 1 of the merge_sort_subarrays_v1() function to each array in the input_arrays list using a list comprehension
sorted_arrays_v1 = [merge_sort_subarrays_v1(array) for array in input_arrays]

# Print the results of Version 1 for each array in sorted_arrays_v1
print("Merged Technique V1:")
for index, array in enumerate(sorted_arrays_v1, start=1):
    print(f"Array_{index} = {array}")
