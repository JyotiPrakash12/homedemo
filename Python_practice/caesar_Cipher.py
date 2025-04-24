alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type encode to encrypt or decode to decrypt\n")
text = input("Enter your text\n").lower()
shift = int(input("Enter the shift amount\n"))



def encrypt(original_text,shift_amount):
    cipher_text = ""

    for char in original_text:
        shifted_postion = alphabet.index(char) + shift_amount
        print(shifted_postion)
        shifted_postion = shifted_postion % len(alphabet)
        cipher_text+=alphabet[shifted_postion]
        print(cipher_text)
    
encrypt(original_text= text, shift_amount=shift)

