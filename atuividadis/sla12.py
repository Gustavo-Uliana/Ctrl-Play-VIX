salario = float(input("Qual o seu salário: "))

if salario <= 900:

    print("O seu salário é de: ", salario)
    print("Seu FGTS foi de 0")
    print("Seu salário final é de ", salario)

elif salario<= 1500:
    fgts = int(input("Quanto foi seu FGTS: "))
    sf = (salario - fgts)

    print("O seu salário é de: ", salario)
    print("Seu FGTS foi de ", fgts)
    print("Seu salário final é de ", sf)

elif salario <= 2500:
    fgts = int(input("Quanto foi seu FGTS: "))
    sf = (salario - fgts)

    print("O seu salário era de: ", salario)
    print("Seu FGTS foi de ", fgts)
    print("Seu salário final é de: ", sf)

elif salario > 2500:
    fgts = int(input("Quanto foi seu FGTS: "))
    sf = (salario - fgts)

    print("O seu salário era de: ", salario)
    print("Seu reajuste foi de ", fgts)
    print("Seu salário final é de: ", sf)