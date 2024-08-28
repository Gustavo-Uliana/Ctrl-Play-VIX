num1 = float(input("1° número: "))
num2 = float(input("2° número: "))
num3 = float(input("3° número: "))

if num1 > num2 > num3:
    print("O 1° é o maior, o 2° é o do meio e o 3° é o menor")

elif num3 < num1 < num2:
    print("O 2° é o maior, o 1° é o do meio o 3° é o menor")

elif num1 < num2 < num3:
    print("O 3° é o maior, o 2° é o do meio e o 1° é o menor")

elif num2 > num3 > num1:
    print("O 2° é o maior, o 3° é o do meio e o 1° é o menor")

elif num1 > num3 > num2:
    print("O 1° número é o maior, o 3° é o do meio o 2° é o menor")

elif num3 > num1 > num2:
    print("O 3° é o maior, o 1° é o do meio o 2° é o menor")