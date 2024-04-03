cipher = ""
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key (an integer): "))
for ch in text:
    # cipher+=chr((ord(ch)+key)%(ord("z")+1))
    cipher += chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
    
print("Encrypted text:", cipher)
