
strUsuario = input("Introduce un par de palabras: ")

lista = strUsuario.split()

if len(lista) > 1:
   
   listaAlrevez = lista[::-1]
   print(listaAlrevez)
else:
    print("Tiene que ser más de una palabra")

