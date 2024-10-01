# Program to print the lyrics of the song "Old MacDonald." 

def lyrics(animal:str,sound:str)->None:
    print(f"----------------THIS IS FOR {animal.upper()} --------------------")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh! ")
    print(f"With a {sound}, {sound} here and a {sound}, {sound} there.")
    print(f"Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! ")

def main()->None:
    animals:list(str)=["cow","pig","duck","horse","lamb"]
    sounds:list(str)=["moo","oink","quack","neigh","baa"]

    for i in range(len(animals)):
        lyrics(animals[i],sounds[i])

main()