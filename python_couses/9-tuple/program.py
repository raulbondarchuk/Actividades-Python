
data = (4, 6, 7, 3, 6, True, 5.6, "Hello")

# data[0] = 5 NO
print(data[1:5])

print(data.count(6))
print(data.count(111))
print(len(data)) 

for el in data:
    print(el)

nums = [5, 7, 8]

new_data = tuple(nums)
print(new_data)

word = tuple("Hello, world")
print(word)