nums = [12,345,2,6,7896]
#Time complexity O(n) and Space complexity is O(1)
count = 0
for item in nums:
    if len(str(item)) % 2 == 0:
        count += 1
print(count)
