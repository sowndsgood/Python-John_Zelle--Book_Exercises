# Average length of words
def main()->None:
    #User input for sentence
    sentence:str=input("Enter the sentence:")
    words=sentence.split(' ')
    sum:int=0
    for i in words:
        length:int=len(i)
        sum+=length    
    print("The average word length is:",sum/len(words))

main()