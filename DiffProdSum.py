n = 234
productofNumbers = 1
sumOfNumbers = 0
diff = 0

#Time Complexity O(n) and Space Complexity is O(1)
for item in str(n):
    productofNumbers = productofNumbers * int(item)
    sumOfNumbers = sumOfNumbers + int(item)
    diff = productofNumbers - sumOfNumbers

print(diff)


