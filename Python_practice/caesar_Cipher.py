alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(original_text,shift_amount):
#     cipher_text = ""
#     for char in original_text:
#         shifted_pos = alphabet.index(char)+shift_amount
#         print(shifted_pos)
#         shifted_pos = shifted_pos % len(alphabet)
#         print(shifted_pos)
#         cipher_text += alphabet[shifted_pos]
#         print(f"encoded text is : {cipher_text}")


# def decrypt(original_text,shift_amount):
#     caesar_decrypt = ""
#     for letter in original_text:
#         shifted_pos = alphabet.index(letter)-shift_amount
#         print(shifted_pos)
#         shifted_pos = shifted_pos % len(alphabet)
#         caesar_decrypt+= alphabet[shifted_pos]
#         print(f"Decoded text is {caesar_decrypt}")

   
# encrypt(original_text= text, shift_amount=shift)
# decrypt(original_text= text, shift_amount=shift)

def ceaser(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount*=-1
    for char in original_text:
        if char not in alphabet:
            cipher_text += char
        else:
            
            shifted_pos = alphabet.index(char)+shift_amount
            print(shifted_pos)        
            # shifted_pos = shifted_pos % len(alphabet)
            print(shifted_pos)
            cipher_text += alphabet[shifted_pos]
        print(f"{encode_or_decode}d text is : {cipher_text}")
      
should_continue = True
while should_continue:

    direction = input("Type encode to encrypt or decode to decrypt\n").lower()
    text = input("Enter your text\n").lower()
    shift = int(input("Enter the shift amount\n"))

    ceaser(original_text=text, shift_amount= shift, encode_or_decode= direction)
    user_continue = input("Type yes to Continue or no to quit: \n").lower()
    if user_continue == "no":
        should_continue = False
        print("Goodbye")



