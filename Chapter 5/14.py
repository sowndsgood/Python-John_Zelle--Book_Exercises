# Word Count (wc) program in Unix and Linux Systems

def main()->None:

    #User input for file name
    file_name=input("Enter the file name:")
    input_file=open(file_name,'r')

    lines:list=[]
    words:list=[]
    characters:int=0

    for line in input_file:
        lines.append(line.strip())
        words.extend(line.split())
    
    for word in words:
        characters+=len(word)

    print("The lines count is",len(lines))
    print("The words count is",len(words))
    print("The character count is",characters)

main()