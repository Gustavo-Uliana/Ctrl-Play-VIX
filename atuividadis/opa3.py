nome = input("Qual seu nome: ")

x = "sla"

idade = int(input("Qual sua idade: "))

sal = float(input("Qual seu salário: "))

sexo = input("Qual seu sexo: ")

ec = input("Qual seu estado civil: ")

if nome >= x:
    print("Tudo certo!")

if idade >= 0 or idade <= 150:
    print("Tudo certo!")

if sal != 0:
    print("Tudo certo!")

if sexo == "f" or sexo == "m":
    print("Tudo certo!")

if ec == "s" or ec == "c" or ec == 'v' or ec == 'd':
    print("Tudo certo!")