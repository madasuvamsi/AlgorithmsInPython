A=[1,2,3,None,None,None,None]

B=[2,4,6,100]

c=[None]*(len(a)+len(B))

idxOne=0
idxTwo=0

K=0

while idxTwo<len(A) and idxTwo<len(B):
    first=A[idxOne]
    second=B[idxTwo]

    if first is        None:
        if first<=second:
            c.append(first)
            idxOne+=1
    else:
        c.append(second)
        idxTwo+=1
print(c)

# == Question ==
#
# Given
# a
# sequence
# of
# integers and an
# integer
# total
# target,
# return whether
# a
# contiguous
# sequence
# of
# integers
# sums
# up
# to
# target.
#
# == =Example == =
#
# [1, 3, 1, 4, 23], 8: True(because
# 3 + 1 + 4 = 8)
# [1, 3, 1, 4, 23], 7: False
#
# [1, 2, 3], 5: True
