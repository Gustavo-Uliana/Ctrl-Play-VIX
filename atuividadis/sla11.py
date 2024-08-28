salario = float(input("Qual o seu salário: "))

if salario <= 280:
    sf = (((20 / 100)* salario) + salario)

    print("O seu salário era de: ", salario)
    print("Seu reajuste foi de 20")
    print("O seu aumento foi de 20%")
    print("Seu salário final é de: ", sf)

elif salario > 280 and salario <= 700:
    sf = (((15 / 100)* salario) + salario)

    print("O seu salário era de: ", salario)
    print("Seu reajuste foi de 15")
    print("O seu aumento foi de 15%")
    print("Seu salário final é de: ", sf)

elif salario > 700 and salario <= 1500:
    sf = (((10 / 100)* salario) + salario)

    print("O seu salário era de: ", salario)
    print("Seu reajuste foi de 10")
    print("O seu aumento foi de 10%")
    print("Seu salário final é de: ", sf)

elif salario < 1500:
    sf = (((5 / 100)* salario) + salario)

    print("O seu salário era de: ", salario)
    print("Seu reajuste foi de 5")
    print("O seu aumento foi de 5%")
    print("Seu salário final é de: ", sf)