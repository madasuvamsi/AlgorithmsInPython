n = 234
productofNumbers = 1
sumOfNumbers = 0
diff = 0
for item in str(n):
    productofNumbers = productofNumbers * int(item)
    sumOfNumbers = sumOfNumbers + int(item)
    diff = productofNumbers - sumOfNumbers

print(diff)


