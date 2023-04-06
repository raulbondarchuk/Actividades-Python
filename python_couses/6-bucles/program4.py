
# Нахождение определенного символа в строке
found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)
