'''
Напишите программу, которая будет реализовывать простую игру "Камень, ножницы, бумага".
Программа должна попросить пользователя ввести "камень", "ножницы" или "бумагу", а затем случайным образом выбрать один из этих вариантов и определить победителя. Правила игры следующие:

- камень побеждает ножницы;
- ножницы побеждают бумагу;
- бумага побеждает камень.

Если выбор пользователя и компьютера совпадает, игра заканчивается вничью.
После каждого раунда программа должна выводить на экран выбор пользователя, выбор компьютера и результат раунда (победа пользователя, победа компьютера или ничья).
Игра должна продолжаться до тех пор, пока пользователь не захочет выйти.
'''
import random

def randomNumber():
    randomNumberStr = "123"

    randomNumber = int(random.choice(randomNumberStr))
    return randomNumber


menuJuego = ''' 
"KAMEN-NOZNICI-BUMAGA"
--------------MENU-----------------
1. Kamen
2. Noznici
3. Bumaga
-----------------------------------
'''
print(menuJuego)
opcionUserStr = input("Tu opción? (1,2 o 3): ")
opcionUser = int(opcionUserStr)

juegoGanado = 0
opcionOrdenador = randomNumber()

if opcionUser == 1:
    if opcionOrdenador == 2:
        juegoGanado = 1
    elif opcionOrdenador == 3:
        juegoGanado = -1
elif opcionUser == 2:
    if opcionOrdenador == 1:
        juegoGanado = -1
    elif opcionOrdenador == 3:
        juegoGanado = 1
elif opcionUser == 3:
    if opcionOrdenador == 1:
        juegoGanado = 1
    elif opcionOrdenador == 2:
        juegoGanado = -1

if juegoGanado == 1:
    print("Has Ganado!")
elif juegoGanado == -1:
    print("Has perdido!")
else:
    print("NADIE HA GANADO")

print(opcionUser, " " ,opcionOrdenador)
