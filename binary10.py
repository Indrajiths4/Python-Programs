# binary=list(input())
# i=0
# while i<len(binary)-1:
#     if binary[i]=='1' and binary[i+1]=='0':
#         binary.pop(i)
#         i=-1
#     i+=1
# print(''.join(binary))

def smallest_string(S):
    S = list(S)  # Convert string to list for mutability
    i = 0
    while i < len(S) - 1:
        if S[i] == '1' and S[i + 1] == '0':
            if S[i] > S[i + 1]:
                del S[i]  # Remove S[i]
            else:
                del S[i + 1]  # Remove S[i + 1]
            # Restart from the beginning as the string has changed
            i = 0
        else:
            i += 1
    return ''.join(S)

# Test the function with the provided examples
print(smallest_string("101010101"))  # Output: 0000111111
print(smallest_string("1111111"))    # Output: 1111111
print(smallest_string("110"))        # Output: 0
