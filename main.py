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