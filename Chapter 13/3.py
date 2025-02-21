#Recursive Palindrome Function

def palindrome(phrase):

    while True:
        if len(phrase)<2:
            return True
        if phrase[0]==phrase[-1]:
            phrase=phrase[1:-1]
            if palindrome(phrase):
                return True
        return False

def main():
    phrase=input("Enter the phrase to check whether palindrome or not:")
    phrase=phrase.lower()
    print(phrase)
    phrase=list(phrase)

    n=0
    while phrase and n<len(phrase):
        if phrase[n] in [" ","?","!","@","#","$","%","&","(",")","[","]",":",";","/",","]:
            del phrase[n]
        else:
            n+=1

    if palindrome(phrase):
        print("Palindrome")
    else:
        print("Not a Palindrome")

main()