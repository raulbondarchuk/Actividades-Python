nums1 = [5,7,8,1,5,2,6]

min = nums1[0]

for el in nums1:
    if el < min:
        min = el
        
print(min)

nums2 = [5.1,7.6,8.1,1.6,5.7,2.1,6.9]

min2 = nums2[0]

for el in nums2:
    if el < min2:
        min2 = el
        
print(min2)
# - - - - - - - - - - - - - - - - - - - -
def minimalNumber(listNumbers):
    minValue = listNumbers[0]
    for el in listNumbers:
        if el < minValue:
            minValue = el
    return minValue

numbers = [1,6,2,8,23,6,2,123,6,1,0.9,7.8,0.9,0.1,111]
minNumber = minimalNumber(numbers)

print(minNumber)