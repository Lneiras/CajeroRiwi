#cajero

saldo = int(100)

print("bienvenido a tu cajero de confianza")

#opciones
while True:
    print("1. consultar saldo",
        "2. retirar", 
        "3. depositar",
        "4. salir",
        sep="\n")

    opciones = int(input("Que operacion deseas realizar el día de hoy"))

    #conultar saldo
    if opciones == 1 :
        print("su saldo es: ", saldo)


    #retirar saldo
    elif opciones == 2 :
        while True:
            Montoaretirar = int(input("Ingresa el monto que deseas retirar :"))
            if Montoaretirar >saldo :
                print("saldo insuficiente")
                continue
            elif Montoaretirar <= 0:
                print("has ingresado un monto errado, intentalo de nuevo")
                continue
            else:
                saldo = saldo - Montoaretirar
                print("retiro exitoso")
                print("tu nuevo saldo es: ", saldo)
                break
                

    #depositar saldo
    elif opciones == 3 :
        while True:
            Monto_a_depositar = int(input("Ingresa el valor que deseas depositar: "))
            if Monto_a_depositar <= 0:
                print("has ingresado un monto errado, intentalo de nuevo")
                continue
            else:
                saldo = saldo + Monto_a_depositar
                print("deposito exitoso",
                    "Tu nuevo saldo es: ", saldo,
                    sep="\n")
                break
    

    #salir          
    elif opciones == 4 :
        print("Gracias por utilizar nuestros servicios",
            "Ten un buen día",
            sep="\n")
        break

    else:
        print("opcion no valida")
        print("intentalo de nuevo")
