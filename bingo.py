from random import random
import random
carton=[]
continuar=True

print("Bienvenido al BINGO! Pruebe suerte con sus números favoritos!!")

while continuar:
    

    while len(carton) < 5:

        numeros=input("Ingrese un numero entre el 1 y el 75: ").strip()

        while numeros.isdigit() and numeros != "":

            numeros_int=int(numeros)

            while numeros != '':

                if numeros_int >= 1 and numeros_int <= 75:
                    if len(carton) == 0:
                        carton.append(numeros_int)
                        numeros=""
                        break
                    val=0
                    for i in carton:
                        if i == numeros_int:
                            print("Número ya en el cartón.")
                            numeros=""
                            val=1
                            break
                        else:
                            val=0
                    if val==0:
                        carton.append(numeros_int)
                        numeros=""
                        break
                else:
                    print("Número no válido. Pruebe de nuevo")
                    numeros=""
                    break
        print(carton)

    bingo=[]

    while len(bingo) < 75:
        numero_random=random.randint(1,75)
        val=0
        for i in bingo:
            if i == numero_random:
                val=1
                break
            else:
                val=0
    
        if val==0:
            bingo.append(numero_random)
            print("Bolas extraidas: ", bingo)
       
    for i in carton:
        if i in bingo:
            print("Número en el cartón.")
    
    print("Fin del juego")
    bingo=[]
    carton=[]
    continuar=input("Deseas volver a jugar? (si/no): ").lower()
    if continuar == "no":
        continuar=False

