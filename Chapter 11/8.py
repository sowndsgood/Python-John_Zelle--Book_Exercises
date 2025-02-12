# Remove duplicates function

def removeDuplicates(my_list):
    unique=[]
    i=0
    while i<len(my_list):
        if my_list[i] in unique:
            del my_list[i]
        else:
            unique.append(my_list[i])
            i+=1

def main()->None:
    
    my_list=[1,2,3,4,5,3,4,3,4]

    removeDuplicates(my_list)

    print(my_list)

main()
