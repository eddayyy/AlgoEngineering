import json
import heapq

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        arrays = json.load(file)
    return arrays

# V1: List of smallest items method
def merge_sort_subarrays_v1(array):
    merged_array = []
    subarray_indices = [0] * len(array)
    
    while True:
        smallest_items = []
        for i, subarray in enumerate(array):
            if subarray_indices[i] < len(subarray):
                smallest_items.append((subarray[subarray_indices[i]], i))
        
        if not smallest_items:
            break
        
        min_item, min_index = min(smallest_items)
        merged_array.append(min_item)
        subarray_indices[min_index] += 1
    
    return merged_array

# V2: Min-heap method
def merge_sort_subarrays_v2(array):
    merged_array = []
    min_heap = []
    
    for i, subarray in enumerate(array):
        if subarray:
            heapq.heappush(min_heap, (subarray[0], i, 0))
    
    while min_heap:
        val, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(val)
        
        if element_idx + 1 < len(array[array_idx]):
            heapq.heappush(min_heap, (array[array_idx][element_idx + 1], array_idx, element_idx + 1))
    
    return merged_array

input_filename = "in2C.txt"
input_arrays = read_input_from_file(input_filename)

sorted_arrays_v1 = [merge_sort_subarrays_v1(array) for array in input_arrays]
sorted_arrays_v2 = [merge_sort_subarrays_v2(array) for array in input_arrays]

print("Merged Technique V1:")
for index, array in enumerate(sorted_arrays_v1, start=1):
    print(f"Array_{index} = {array}")

print("\nMerged Technique V2:")
for index, array in enumerate(sorted_arrays_v2, start=1):
    print(f"Array_{index} = {array}")
