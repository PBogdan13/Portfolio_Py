

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cesar(star_text,shift_amount, direction_cipher):
    end_text = ""
    if direction_cipher == "decode":
            shift_amount*=-1
    for letter in star_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text+= alphabet[new_position]
    print(f"The {direction_cipher} test is {end_text}")       
          
cesar(star_text=text,shift_amount=shift, direction_cipher=direction)







