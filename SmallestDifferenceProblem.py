
arrayOne=[-1, 5, 10, 20, 3]#after sorting [-1,3,5,20,20]
arrayTwo=[26, 134, 135, 15, 17]#after sorting [15,17,26,134,135]

outputarray=[0,0]

arrayOne.sort()
arrayTwo.sort()

idxOne=0
idxTwo=0

smallest=float('inf')
current=float('inf')

smallestpair=[0,0]

while idxOne<len(arrayOne) and idxTwo<len(arrayTwo):
    first=arrayOne[idxOne]
    second=arrayTwo[idxTwo]
    if first < second:
        current = second-first
        idxOne+=1
    elif second < first:
        current=first-second
        idxTwo+=1
    else:
        smallestpair[0]=first
        smallestpair[1]=second
    if smallest>current:
        smallest=current
        smallestpair[0] = first
        smallestpair[1] = second

print(smallestpair)



#TimeComplexity O(n2) spacecomplexity O(1)
# temp=float('inf')
#
# for i in arrayOne:
#     first=i
#     for j in arrayTwo:
#         second=j
#         absdiff=abs(first-second)
#         if absdiff<temp:
#             temp=absdiff
#             outputarray[0]=first
#             outputarray[1]=second
#
#
# print(temp)
# print(outputarray)

