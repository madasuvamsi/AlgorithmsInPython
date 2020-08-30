inputarray=[1,2,3,4,5]

def binarySearch(array,searchelement):
    start = 0;
    end=len(array)-1
    while start<=end:
        mid =int((start+end)/2)
        if(searchelement==array[mid]):
            return mid
        elif(searchelement<array[mid]):
            end=mid-1
        elif(searchelement>array[mid]):
            start=mid+1
    return -1

searchele = int(input("Enter search element:"))

result=binarySearch(inputarray,searchele)

if(result==-1):
    print("Element not found")
else:
    print("Element is found at "+str(result)+" position")
