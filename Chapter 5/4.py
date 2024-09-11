# Acronym for Phrase
def main()->None:
    #Input for phrase
    phrase:str=input("Enter the phrase:")
    acronym:str=''
    for word in phrase.split():
        acronym+=word[0]
    print("The Acronym is:",acronym.upper())

main()
