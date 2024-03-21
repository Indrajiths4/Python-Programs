binary_input = input("Enter a binary number: ")

# Check if the input is a valid binary number
if set(binary_input) <= {'0', '1'}:
    # Padding the binary number with zeros if necessary to make its length a multiple of 3
    while len(binary_input) % 3 != 0:
        binary_input = '0' + binary_input

    octal_number = ''
    # Converting binary digits in groups of 3 to octal digits
    for i in range(0, len(binary_input), 3):
        binary_group = binary_input[i:i+3]
        octal_digit = int(binary_group, 2)
        octal_number += str(octal_digit)

    print("Octal equivalent:", octal_number)
else:
    print("Invalid binary number entered.")
