#Caesar cipher Encoding and Decoding
#Function for encoding
def encode(string,key)->str:
    output:str=''
    for i in string:
        output+=chr(ord(i)+key)
    return output

#Function for decoding
def decode(output,key)->str:
    decoded:str=''
    for i in output:
        decoded+=chr(ord(i)-key)
    return decoded

def main()->None:
    #Input string
    string:str=input("Enter the string:")
    key:int=int(input("Enter the key:"))
    output:str=encode(string,key)
    print("Output is:",output)
    decoded:str=decode(output,key)
    print("The decoded text is:",decoded)
main()