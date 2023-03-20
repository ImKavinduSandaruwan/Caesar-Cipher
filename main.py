#Coded by Kavindu Sandaruwan
letter_list = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(text,shift_amount):
    encode_text = ""
    for i in text:
        if i in letter_list:
            index_of_letter = letter_list.index(i)
            new_letter = letter_list[index_of_letter + shift_amount]
            encode_text += new_letter
        else:
            encode_text += i
    print("Here is your encrypted msg: ",encode_text)
        
def decode(encode_text,shift_amount):
    decode_text = ""
    for i in encode_text:
        if i in letter_list:
            index_of_letter = letter_list.index(i)
            new_letter = letter_list[index_of_letter - shift_amount]
            decode_text += new_letter
        else:
            decode_text += i
    print("Here is your decrypted msg: ",decode_text)
        
    
while True:
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if option == "encode":
        msg = input("Enter your message: ").lower()
        shift = int(input("Enter the shift number: "))
        encode(text=msg, shift_amount=shift)


    elif option == "decode":
        msg = input("Enter your message: ").lower()
        shift = int(input("Enter the shift number: "))
        decode(encode_text=msg, shift_amount=shift)

    else:
        print("Please enter valid input")
        continue

    run_again = input("Type 'yes' if you want to run agin. Otherwise type'no'.").lower()
    if run_again != "yes":
        print("Thank you have a nice day")
        break
