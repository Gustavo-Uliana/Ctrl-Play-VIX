nota1 = float(input("Qual foi sua 1ª nota: "))
nota2 = float(input("Qual foi sua 2ª nota: "))

notamedia = (nota1 + nota2) / 2

if notamedia >= 7:
    print("Aprovado")
elif notamedia >= 10:
    print("Aprovado com distinção")
elif notamedia < 7:
    print("Você é um ASNO! Reprovado!")