def FibNumber(n):
    if n<=1:
       return n
    else:
        return FibNumber(n-1)+FibNumber(n-2)


n=int(input("Enter the Number"))

print(FibNumber(n))