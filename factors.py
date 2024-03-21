# Input number from the user
num = int(input("Enter a number: "))

print("Factors of", num, "are:")

# Iterate from 1 to the number
for i in range(1, num + 1):
    # Check if the current number 'i' divides 'num' without leaving a remainder
    if num % i == 0:
        print(i)
