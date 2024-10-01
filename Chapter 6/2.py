#Program to print the lyrics for ten verses of "The Ants Go Marching."

def lyrics(activity,number)->None:
    print(2*f"The ants go marching {number} by {number}, hurrah! hurrah!\n")
    print(f"The ants go marching {number} by {number},")
    print(f"The little one stops to {activity}, ")
    print("And they all go marching down ...")
    print("In the ground ...") 
    print("To get out .... ")
    print("Of the rain. ")
    print("Boom! Boom! Boom!")

def main()->None:
    number:list[str]=["one","two","three","four","five","six","seven","eight","nine","ten"]
    
    for i in range(10):
        activity=input("Enter a activity:")
        lyrics(activity,number[i])

main()