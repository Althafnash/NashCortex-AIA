Alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
key_code = input("Enetr Key code : ")
Message = input("Enter Password : ")

def encrypt():
    encrypted_message = ""
    for letter in Message:
        if letter.upper() in Alpha:
            index = Alpha.index(letter.upper())
            new_index = (index + key_code) % len(Alpha)
            encrypted_letter = Alpha[new_index]
            if letter.islower():
                encrypted_message += encrypted_letter.lower()
            else:
                encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    
    return encrypted_message

encrypted_message = encrypt()
print(f"Original message: {Message}")
print(f"Encrypted message: {encrypted_message}")
