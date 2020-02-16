x=[1,2]

subset=[[]]

for ele in x:
    for i in range(len(subset)):
        currentlist=subset[i];
        subset.append(currentlist+[ele])

print(subset)

