def divide(a,b):
    if b!= 0:
        valor=a/b
        return valor
    else:
        print("No se puede dividir por cero")
dividendo=input("Primer número: ")
if dividendo.isnumeric():
    dividendo=float(dividendo)
    divisor=input("Segundo número: ")
    if divisor.isnumeric():
        divisor=float(divisor)
        print("El resultado de la división es:",divide(dividendo,divisor))
    else:
        print("Debes escribir números")    
else:
    print("Debes escribir números")