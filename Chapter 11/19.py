# Set class to represent a classical set  using lists and dictionaries.

class Set:

    def __init__(self,elements):
        '''Creates a set'''
        self.elements=elements

    def display(self):
        '''Prints the set'''
        print(self.elements)

    def addElement(self,x):
        '''Adds x to the set'''
        self.elements.append(x)

    def deleteElement(self,x):
        '''Removes x from the set'''
        if x in self.elements:
            self.elements.remove(x)

    def member(self,x):
        '''Returns true if x is in the set and false otherwise'''
        if x in self.elements:
            return True
        else:
            False

    def intersection(self,set2):
        '''Returns a new set with common elements'''
        new=[]
        for element in set2:
            if element in self.elements and element in set2:
                new.append(element)
        return new
    
    def union(self,set2):
        '''Returns a new set with all elements'''
        dict={}
        for i in set2:
            dict[i]=dict.get(i,0)+1
        for i in self.elements:
            dict[i]=dict.get(i,0)+1
        list1=[key for key in dict.keys()]
        return list1

    def subtract(self,set2):
        '''Returns a new set containing all the elements of this set that are not in set2. '''
        for i in set2:
            if i in self.elements:
                self.elements.remove(i)
        return self.elements

def main()->None:
    set=Set([1,3,4,5,6])

    set.addElement(2)
    set.display()

    set.deleteElement(4)
    set.display()

    print(set.member(5))

    print(set.intersection([2,3,4]))

    print(set.union([4,5,6,7,8]))

    print(set.subtract([3,4,5]))

main()