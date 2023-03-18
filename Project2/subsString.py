# Author: Eduardo Nunez
# Author email: 
# Import the json module for loading data from a file
import json

def find_substrings(input_file):
    with open(input_file, "r") as file:
        data = json.load(file)
        
    arrays = data["Inputs"]
    results = {}
    
    for i, (array_key, target_key) in enumerate(zip(["Array1a", "Array2a", "Array3a"], ["Array1b", "Array2b", "Array3b"]), 1):
        array = "".join(arrays[array_key])
        target_terms = arrays[target_key]
        
        output_order = []
        output_array = []
        for term in target_terms:
            index = array.find(term)
            if index != -1:
                output_order.append(index)
                output_array.append(term)
                
        output_order, output_array = zip(*sorted(zip(output_order, output_array)))

        results[f"Output_order{i}"] = output_order
        results[f"Output_array{i}"] = output_array
    
    return results

def print_results(results):
    for i in range(1, len(results)//2 + 1):
        output_order_key = f"Output_order{i}"
        output_array_key = f"Output_array{i}"
        print(f"Array {i}:")
        print(f"  Order: {results[output_order_key]}")
        print(f"  Terms: {results[output_array_key]}")
        print()

input_file = "in2a.txt"
result = find_substrings(input_file)
print_results(result)
