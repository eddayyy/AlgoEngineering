import heapq

with open("in2C.txt", "r") as f:
    lines = f.readlines()

arrays = {}
current_array = None
for line in lines:
    if line.startswith("Array"):
        if current_array:
            arrays[array_name] = list(heapq.merge(*current_array))
        array_name = line.strip().split()[0]
        current_array = []
    elif "[" in line:
        current_array.append([int(s.strip()) for s in line.strip()[1:-1].split(",")])
if current_array:
    arrays[array_name] = list(heapq.merge(*current_array))

Array_1 = sorted(arrays['Array_1'])
Array_2 = sorted(arrays['Array_2'])
Array_3 = sorted(arrays['Array_3'])

print("Array_1:", Array_1)
print("Array_1:", Array_2)
print("Array_3:", Array_3)
