#class carro (): 
    #def __init__(self,marca, ano, cor):
        #self.marca = marca
        #self.ano = ano
        #self.cor = cor

#marca_inp = input("qual a marca do carro")
# ano_inp = input("qual o ano do carro")
# cor_inp = input("qual a cor do carro")

# carro= carro(marca_inp,ano_inp,cor_inp)
# print(f"\nmarca:{carro.marca}\nano:{carro.ano}\ncor:{carro.cor}")

# #ex2

#


# #ex3
# contador = 1

# while contador <= 5:
#     print(contador)

# #ex4

# resposta = ""

# while resposta != "sair":
#     resposta = input("digite algo (ou 'sair' para finalizar): ")

#     print("voce decidiu sair. programa encerrado.")

#     #ex5

# contador = 1

# while resposta != "sair":
#       resposta = input("digite algo (ou 'sair' para finalizar): ")

# print("voce decidiu sair. programa encerrado.")
# #EX6
# import random

# # Gera um número aleatório entre 1 e 100
# numero_secreto = random.randint(1, 100)

# print("Bem-vindo ao jogo de adivinhação!")
# print("Tente adivinhar o número secreto entre 1 e 100.")

# while True:
#     # Solicita que o usuário insira um palpite
#     palpite = int(input("Digite seu palpite: "))

#     if palpite < numero_secreto:
#         print("O número secreto é maior!")
#     elif palpite > numero_secreto:
#         print("O número secreto é menor!")
#     else:
#         print("Parabéns! Você adivinhou o número!")
#         break

#     #EX7

#     # Definindo o nome de usuário e senha corretos
# usuario_correto = "admin"
# senha_correta = "1234"

# while True:
#     # Solicita o nome de usuário e a senha do usuário
#     usuario = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha: ")

#     # Verifica se ambos estão corretos
#     if usuario == usuario_correto and senha == senha_correta:
#         print("Acesso concedido!")
#         break
#     else:
#         print("Nome de usuário ou senha incorretos. Tente novamente.")

#    #EX8

soma_total = 0

print("Digite números para somar. Para encerrar e ver o total, digite 0.")

while True:
    numero = float(input("Digite um número: "))
    
    if numero == 0:
        break  # Encerra o loop quando o usuário digita 0
    
    soma_total += numero  # Adiciona o número à soma total

print(f"A soma total é: {soma_total}")




