'''par o impar mejorada'''

def par_o_impar ():
    print("Hello there")
    print("indicandome el numero podre decirte si el numero es par o impar")
    
    while True:
        try:
            numero = int(input("decidme un numero entre el 1 y el 1000:  "))

            if 1 <= numero <= 1000:
                break
            else:
                print('te dije entre el 1 y el 1000 moron, intentalo de nuevo')
        except ValueError:
            print('ingresa un valor numerico pendejazo')


    if numero % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es impar')

par_o_impar()


#epaleeeeee