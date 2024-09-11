# Problem Number 11 with Text Input and Output
def main()->None: 

    input_file=open('13input.txt','r')
    output_file=open('13output.txt','w')

    print("This program illustrates a chaotic function",file=output_file) 

    input_details:list=[]
    for line in input_file:
        input_details.append(line.strip())

    #Input from user
    x:float = float(input_details[0]) #Number between 0 and 1
    y:float = float(input_details[1]) #Number between 0 and 1
    z:int=int(input_details[2]) #Number of iterations

    #Table printing
    print("index      {0}       {1}".format(x,y),file=output_file)
    for i in range(z): 
        a:float=3.9*x*(1-x)
        b:float=3.9*y*(1-y)
        print("{0:^6}   {1:8.6f}    {2:8.6f}".format(i,a,b),file=output_file)
        x:float=a
        y:float=b

    input_file.close()
    output_file.close()

main()