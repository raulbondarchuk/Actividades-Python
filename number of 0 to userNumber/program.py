def ErrorMessage():
    return "Valor introducido no es un número"

userNumberStr = input("Introduce un número: ")
contador = 0
try: 
    userNumber = int(userNumberStr)

    if userNumber > 0:
        while contador < userNumber:
                contador += 1
                print(contador)
    else:
        print(ErrorMessage())
except ValueError:
    print(ErrorMessage())


    

