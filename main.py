from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            if direction == "encode":
                new_position = position + shift
            else:
                new_position = position - shift
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_text += i
    if direction == "encode":
        print(f"The encoded text is {new_text}")
    else:
        print(f"The decoded text is {new_text}")


print(logo)
run_again = True
while run_again:
# User screen
    #print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

# Call function
    caesar(text, shift, direction)

    result = input("Would you like to run the cipher again? yes or no: ")
    if result == "no":
        run_again = False