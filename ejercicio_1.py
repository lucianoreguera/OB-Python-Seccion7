import operaciones.operaciones as op


a: int = int(input("Ingresar un número: "))
b: int = int(input("Ingresar un número: "))
operacion: str = input("Ingresar operación a realizar[+,-,*,/]: ")

if (operacion == '+'):
    print(str(a) + operacion + str(b) + "=" + str(op.sumar(a, b)))
elif(operacion == '-'):
    print(str(a) + operacion + str(b) + "=" + str(op.restar(a, b)))
elif(operacion == '*'):
    print(str(a) + operacion + str(b) + "=" + str(op.multiplicar(a, b)))
elif(operacion == '/'):
    print(str(a) + operacion + str(b) + "=" + str(round(op.dividir(a, b))))
else:
    print("Operador no reconocido")