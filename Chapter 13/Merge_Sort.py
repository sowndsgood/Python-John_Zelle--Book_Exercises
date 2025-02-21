def merge(arr1,arr2,arr):
    i1=0 
    i2=0
    i3=0

    n1=len(arr1)
    n2=len(arr2)

    while i1<n1 and i2<n2:
        if arr1[i1]<arr2[i2]:
            arr[i3]=arr1[i1]
            i1+=1
        else:
            arr[i3]=arr2[i2]
            i2+=1
        i3+=1

    while i1<n1:
        arr[i3]=arr1[i1]
        i3+=1
        i1+=1

    while i2<n2:
        arr[i3]=arr2[i2]
        i3+=1
        i2+=1

def merge_sort(arr):
    n=len(arr)

    if n>1:
        m=n//2
        arr1=arr[0:m]
        arr2=arr[m:n]
        merge_sort(arr1)
        merge_sort(arr2)

        merge(arr1,arr2,arr)

arr:list[int]=[34,72,5,6,75,1]
merge_sort(arr)
print(arr)