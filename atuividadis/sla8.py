num1 = float(input("1° número: "))
num2 = float(input("2° número: "))
num3 = float(input("3° número: "))

if num1 > num2 > num3:
    print("O 3° é o de melhor preço")

elif num3 < num1 < num2:
    print("O 3° é o de melhor preço")

elif num1 < num2 < num3:
    print("O 1° é o de melhor preço")

elif num2 > num3 > num1:
    print("O 1° é o de melhor preço")

elif num1 > num3 > num2:
    print("O 2° é o de melhor preço")

elif num3 > num1 > num2:
    print("O 2° é o de melhor preço")