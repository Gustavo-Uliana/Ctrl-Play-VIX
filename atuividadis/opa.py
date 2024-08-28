nota = float(input("Qual sua nota: "))

x = 5

while x == 5:
    if nota > 10 or nota < 0:
        print("Formato de Uso Inválido")
        nota = float(input("Qual sua nota: "))
while x == 5:
    if nota <= 10 and nota > 0:
        print("Ok")
    