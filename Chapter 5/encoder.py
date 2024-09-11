#Encoder Program
def main():
    text=input("Enter the text to be encoded:")
    print("Here is the code:")
    for ch in text:
        print(ord(ch),end=' ')
main()