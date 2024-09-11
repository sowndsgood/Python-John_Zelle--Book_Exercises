def main():
    string=input("Enter the encoded numbers:")
    message=""
    for num in string.split(" "):
        ch=int(num)
        message=message+chr(ch)

    print("The decoded message:",message)
main()