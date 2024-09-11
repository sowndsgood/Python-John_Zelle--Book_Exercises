# Count the Number of words
def main()->None:
    sentence:str=input("Enter the sentence:")
    list_of_words:list[str]=sentence.split(' ')
    print("The number of words in the sentence is:",len(list_of_words))

main()