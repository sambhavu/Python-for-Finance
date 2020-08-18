twoSum = 0
threeSum = 0


for i in range(100):
    if i % 2 == 0:
        twoSum = twoSum + i

    if i%3 == 0:
        threeSum = threeSum+i



print(twoSum)
print(threeSum)
