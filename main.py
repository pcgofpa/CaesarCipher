alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    new_text = ""
    for i in text:
        position = alphabet.index(i)
        if direction == "encode":
            new_position = position + shift
        else:
            new_position = position - shift
        new_letter = alphabet[new_position]
        new_text += new_letter
    if direction == "encode":
        print(f"The encoded text is {new_text}")
    else:
        print(f"The decoded text is {new_text}")

caesar(text, shift, direction)
