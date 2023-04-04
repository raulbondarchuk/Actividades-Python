
userNumberStr = input("Introduce el número necesario: ")

sumRest = 0

try:
    userNumber = int(userNumberStr)
    print("**Numero introducido es:", userNumber,"**")
    if userNumber > 0:
        contador = 0
        while contador < userNumber:
            contador = contador + 1

            remainder = userNumber % contador
            if remainder == 0: # Si es 0 - divide sin problemas. Si es 1 pues si que divide; pero tiene el resto
                print(contador)

    else:
        print("Numero introducido incorrecto")

except ValueError:
    print("Numero introducido incorrecto")