import operaciones 
num1=int(input("Ingresa el primer numero "))
num2=int(input("Ingresa el segundo numero "))


def main():
    multiplica=operaciones.multiplicar(num1,num2)
    print("El resultado es: ", multiplica)


if  __name__=="__main__":
    main()