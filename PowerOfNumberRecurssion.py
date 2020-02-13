#Time Compelity is 0(logn) and Spacecomplexty is O(n)
def powNumber(x,n):
    if n==0:
        return  1
    elif n%2 == 0:
        y=powNumber(x,n/2)
        return y*y
    else:
        return x*powNumber(x,n-1)


x=int(input("Enter the number:"))
n=int(input("Enter the power to be raised:"))

result=powNumber(x,n)

print("The Result is ",result)