

def run_encoding(S):
    n = len(S)  
    i = 0
    while i < n - 1:
        count = 1
        while i < n - 1 and S[i] == S[i+1]:
            count += 1
            i += 1
        i += 1
        if count == 1:
            print(S[i-1], end="")
        else:
            print(str(count) + S[i - 1], end="")
            
x = "heloooooooo there"
run_encoding(x)
print()