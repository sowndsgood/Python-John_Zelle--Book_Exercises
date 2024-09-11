def main():
    string=input("Enter the encoded numbers:")
    messages=[] #This is a list"
    for num in string.split(" "):
        ch=int(num)
        messages.append(chr(ch))
    message="".join(messages)
    print("The decoded message:",message)
main() 