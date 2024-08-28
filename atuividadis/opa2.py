nome = input("Qual seu Nome: ")

senha = input("Qual sua senha: ")

x = 1

while x == 1:
    if senha == nome:
        print("Refaça o formulário")
        nome = input("Qual seu Nome: ")
        senha = input("Qual sua senha: ") 

    break   
