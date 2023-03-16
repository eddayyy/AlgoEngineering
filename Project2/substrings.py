# Author: Eduardo Nunez
# Author email: 
import json

def find_substrings(input_file):
    with open(input_file, "r") as file:
        data = json.load(file)
        
    arrays = data["Inputs"]
    results = {}
    
    for i, (array_key, target_key) in enumerate(zip(["Array1a"], ["Array1b"]), 1):
        array = arrays[array_key]
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

input_file = "in2a.txt"
result = find_substrings(input_file)
print(result)
