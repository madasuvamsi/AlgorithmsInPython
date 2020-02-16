randomlist=[-2,10,5,1,-1,6,4]

left=0
right=len(randomlist)-1

sortedarray=[0,0,0,0,0,0,0]

for i in range(len(randomlist)):
    if randomlist[left]<randomlist[right]:
        sortedarray[i]=randomlist[left]
        left+=1
    else:
        sortedarray[i]=randomlist[right]
        right-=1

print(sortedarray)