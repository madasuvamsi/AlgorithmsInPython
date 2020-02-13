def powNumber(x,n):
    if n==0:
        return 1
    else:
        return x*powNumber(x,n-1)

x=int(input("Enter the number:"))
n=int(input("Enter the power to be raised:"))

result=powNumber(x,n)

print("The Result is ",result)