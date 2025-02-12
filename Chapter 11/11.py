# Automated censor program

def check_punc(str):
    for i in str:
        if i in[',''.','!','?',':',';','[',']','{','}']:
            return False
        else:
            return True


def main()->None:

    input_file=input("Enter the input text file:")
    output_file=input("Enter the output file name:")

    infile=open(input_file,'r')
    outfile=open(output_file,'w')

    for line in infile:
        for str in line.split():
            if len(str)==4 and check_punc(str):
                print('****',end=" ",file=outfile)
            else:
                print(str,end=" ",file=outfile)
        print(file=outfile)

    infile.close()
    outfile.close()

main()