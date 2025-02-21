# Selection Sort

def selection_sort(arr)->list[int]:

    n:int=len(arr)

    for i in range(n-1): 
        min=i
        for j in range(i,n): #Looping to find minimum
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    return arr

def main():

    arr:list[int]=[34,72,5,6,75,1]

    sorted_arr:list[int]=selection_sort(arr)
    print(sorted_arr)

main()