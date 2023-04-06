for i in range(1,6,2): # Нвчвльное, конечное, шаг
    print(i)

print("- - - - -")

count = 0

word = "Hello World!"
for i in word:
    if i == "l":
        count += 1

print("Count:", count)
