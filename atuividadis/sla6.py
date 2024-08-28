num1 = float(input("1° número: "))
num2 = float(input("2° número: "))
num3 = float(input("3° número: "))

if num1 > num2 > num3:
    print("O 1° é o maior")

elif num1 < num2 > num3:
    print("O 2° é o maior")

elif num1 < num2 < num3:
    print("O 3° é o maior")