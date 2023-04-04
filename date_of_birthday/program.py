from datetime import *
import os

exitBool = False # salida

while True:
    dateOfUserString = input("Introduce su fecha de nacimiento en formato \"dia/mes/año\". (Ejemplo: 23-04-2001): ")
    dateOfUserString = dateOfUserString.replace("/","-")
    dateOfUserString = dateOfUserString.replace(".","-")

    try:
        dateOfUser = datetime.strptime(dateOfUserString,"%d-%m-%Y").date()

        today = date.today()
        
        dateResultDays = today - dateOfUser
        yearsOld = dateResultDays.days // 365
        
        birthday = dateOfUser.replace(year=dateOfUser.year + yearsOld + 1)

        daysToBirthday = birthday.day - today.day
        print("--------------------------------------------")
        print("Su edad actual es:", yearsOld,"años. Queda para el siguiente cumpleaños:", daysToBirthday, "días. Vas a cumplir:", (yearsOld + 1), "años.")
        print("--------------------------------------------")
    except ValueError:
        print('Fecha "' + dateOfUserString + '" no existe o no está escrita bien')

    exitOfProgram = (input("¿Quieres salir? (S o s): "))
    if exitOfProgram.lower() == "s":
        os.system('cls')
        break
    else:
        os.system('cls')
