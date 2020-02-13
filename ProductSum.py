#Time Complexity is O(n) where n is the elements in the main array and also elements in the special array
#Space Complexity is O(d) where d is the depth of the array
def productSum(array,multiplier=1):
    sum=0
    for element in array:
        if type(element) is list:
            sum+=productSum(element,multiplier+1)
        else:
            sum+=element
    return sum*multiplier

#testcase1
#Time Compexlity is 0(5)--> 1,2, [3,4], 3, 4
#Space Complexity is 0(2)
inputarray= [1,2,[3,4]]
print("Result for test case 1 is",productSum(inputarray))

#testcase2
#Time compelxity is O(6)-->1,2,[3,-4],3,-4,5
#Space Complexity is 0(2)
inputarray1= [1,2,[3,-4],5]
print("Result for test case 2 is",productSum(inputarray1))