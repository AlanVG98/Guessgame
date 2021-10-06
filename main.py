import random
def humanGuess ():
    number = random.randrange(0,10)
    print(number)
    op = -1
    while(number != op):
        op = int(input("Introduce un numero: "))
        if (number == op):
            print("Felicidades ganaste, el numero era {}".format(number))
        else:
            if(number > op): 
                print("Te falto")
            else:
                print("Te pasaste")

def computerGuess():
    #Pensamos en nuestro numero escogi 500
    number = random.randrange(0,1000) #es el de la computadora
    bandera = False 
    
    while(bandera == False):
        print (number)
        print("Este es tu numero?")
        opc= input("Si | No:  ").lower()
        if( opc == "no"):
            print("Tu numero es mayor o menor al mio?")
            opc2 = input("Mayor | Menor: ").lower()
            if (opc2 == "menor"): #En caso que es menor
                newNumber = random.randrange(0,number) #que el de la computadora es mayor
                number = newNumber
            else: #En caso que es mayor
                newNumber = random.randrange(number,1000)
                number = newNumber
        else:
            bandera = True

    
computerGuess()