n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3
print("Media:", media)

if media >= 6:
    print("Aprovado!") 
if (media >= 5.5) & (media <6):
    print("Recuperação!")
else:
    print("Reprovado!")
