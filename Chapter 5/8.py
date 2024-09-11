#Caesar cipher in a circular fashion
#Function for encoding

ALPHABET='abcdefghijklmnopqrstuvwxyz'

def encode(string,key)->str:
    output:str=''
    for i in string:
        if i in ALPHABET:
            index=ALPHABET.index(i)
            new_index=(index+key)%len(ALPHABET)
            output+=ALPHABET[new_index]
        else:
            output+=i
        
    return output

#Function for decoding
def decode(output,key)->str:
    decoded:str=''
    for i in output:
        if i in ALPHABET:
            index=ALPHABET.index(i)
            new_index=(index-key)%len(ALPHABET)
            decoded+=ALPHABET[new_index]
        else:
            decoded+=i
        
    return decoded

def main()->None:

    #Input string
    string:str=input("Enter the string:").lower()
    key:int=int(input("Enter the key:"))

    output:str=encode(string,key)
    print("Output is:",output)

    decoded:str=decode(output,key)
    print("The decoded text is:",decoded)

main()