# Programming Exercise 4 from Chapter 5

def acronym(phrase:str)->str:
    acronym:str=''
    for word in phrase.split():
        acronym+=word[0]
    return acronym.upper()

phrase:str=input("Enter the phrase:")
print("The Acronym is:",acronym(phrase))
