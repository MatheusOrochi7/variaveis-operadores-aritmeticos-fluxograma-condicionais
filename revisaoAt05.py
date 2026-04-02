a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
op = input("Operação(+,-,*,/): ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Operação invalida")