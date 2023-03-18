def run_encoding(S):
    n = len(S)  # Get the length of the input string
    i = 0  # Initialize a counter for the current character index in the string
    encoded_segments = []  # Initialize a list to store the encoded segments

    # Loop through the string
    while i < n:
        count = 1  # Initialize a counter for the number of consecutive characters
        
        # Loop through consecutive characters that are the same
        while i < n - 1 and S[i] == S[i+1]:
            count += 1  # Increment the counter for the number of consecutive characters
            i += 1  # Increment the current character index
        
        i += 1  # Increment the current character index (to skip over the last repeated character)

        # If there was only one consecutive character, append it to the list
        if count == 1:
            encoded_segments.append(S[i-1])
        # If there were multiple consecutive characters, append the count and the repeated character to the list
        else:
            encoded_segments.append(str(count) + S[i - 1])

    # Join and print the encoded segments
    print("".join(encoded_segments))

# Define a test string
x = "choosemeeky and tuition-free"

# Call the run_encoding() function with the test string as an argument
run_encoding(x)
