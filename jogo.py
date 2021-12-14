import random # coso random
import os # me encanta el os


while True:
    os.system('color e')
    print('JUEGO EPICO DE ADIVINAR EL NUMERO')
    o= random.randint(0,5)
    i= int(input('Dime un numero del 0 al 5: '))
    if i == o:
        print('Adivinaste el numero!')
    else:
        print('El numero era', o,' no adivinaste')

    n = str(input('Quieres jugar de vuelta? (y/n)'))

    if n == 'y':
        os.system('cls')
    else:
            break
