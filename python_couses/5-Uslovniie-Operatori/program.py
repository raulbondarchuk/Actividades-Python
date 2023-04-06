user_data = int(input("Introduce el numero: "))

isHappy = True

if isHappy and user_data == 6:
    print("User is Happy")
elif not isHappy or user_data == 5:
    print("User IS NOT Happy")


if user_data != 5:
    print("Is not equal than 5")
    if user_data > 6:
        print("Number is bigger than 5")


# Тернарный оператор
data = input()

number = 5 if data == "Five" else 0 #Ternarnii

if data == "five":
    number = 5
else:
    number = 0

print(number)