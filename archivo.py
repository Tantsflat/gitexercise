'''par o impar'''

def par_o_impar ():
    print("Hello there")
    print("indicandome el numero podre decirte si el numero es par o impar")
    numero = int(input("decidme un numero entre el 1 y el 1000:  "))

    if numero < 1 or numero > 1000:
        print('te dije entre el 1 y el 1000 moron')
    elif numero % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es impar')

par_o_impar()