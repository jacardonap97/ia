numero1=int(input("Ingrese un número: "))
numero2=int(input("Ingrese un número: "))
numero3=int(input("Ingrese un número: "))


if(numero1>=numero2 and numero1>=numero3):
    if(numero2>=numero3):
        print(numero3, numero2, numero1)
    else:
        print(numero2,numero3,numero1)
elif(numero3>=numero2 and numero3>=numero1):
    if(numero2>=numero1):
        print(numero1,numero2,numero3)
    else:
        print(numero2,numero1,numero3)
elif(numero2>=numero1 and numero2 >=numero3):
    if (numero1 >= numero3):
        print(numero3,numero1,numero2)
    else:
        print(numero1,numero3,numero2)
