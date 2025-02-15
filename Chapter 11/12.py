# Censored words

def main():

    input_file=input("Enter the input file name:")
    censored_file=input("Enter the censored words file name:")
    output_file=input("Enter the output file name:")

    infile=open(input_file,'r')
    cenfile=open(censored_file,'r')
    outfile=open(output_file,'w')

    for line in cenfile:
        censored_words=line.split()

    for line in infile:
        words=line.split()

        for word in words:
            if word in censored_words:
                print("*" *len(word),file=outfile,end=' ')
            else:
                print(word,file=outfile,end=' ')
        
        print(file=outfile)

main()