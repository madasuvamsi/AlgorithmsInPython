array=[1, 2, 2, 5, 4]
tomove=2

i=0
j=len(array)-1

while i<j:
    while i<j and array[j]==tomove:
        j-=1
    if array[i]==tomove:
        array[i], array[j]=array[j],array[i]
    i+=1

print(array)